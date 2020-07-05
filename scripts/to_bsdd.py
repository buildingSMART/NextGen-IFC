import os
import re
import sys
import json

from collections import defaultdict

import xmi

try:
    fn = sys.argv[1]
    try:
        OUTPUT = open(sys.argv[2], "w", encoding='utf-8')
    except IndexError as e:
        OUTPUT = sys.stdout
except:
    print("Usage: python to_po.py <schema.xml>", file=sys.stderr)
    exit()

xmi_doc = xmi.doc(fn)
bfn = os.path.basename(fn)

schema_name = xmi_doc.by_tag_and_type["packagedElement"]['uml:Package'][1].name.replace("exp", "").upper()
schema_name = "".join(["_", c][c.isalnum()] for c in schema_name)
schema_name = re.sub(r"_+", "_", schema_name)
schema_name = schema_name.strip('_')

def generate_definitions():
    """
    A generator that yields tuples of <a, b> with
    a: location in file
    a: a fully qualifying key as tuple
    b: the documentation string
    """
    classifications = defaultdict(dict)
    data = {
        'Domain': {
            'Name': 'IFC',
            'Version': schema_name,
            
            'Classifications': classifications
        }
    }
    
    class_name_to_node = {}
    
    for c in xmi_doc.by_tag_and_type["element"]["uml:Class"]:
        class_name_to_node[c.name] = c
        stereotype = (c/"properties")[0].stereotype
        if stereotype is not None: 
            stereotype = stereotype.lower()  
        if stereotype and stereotype.startswith("pset"):
            pset_name = c.name
            try:
                class_idref = (c|"links"|"Realisation").start
            except ValueError as e:
                print("WARNING:", pset_name, "has no associated class", file=sys.stderr)
                continue

            class_name = xmi_doc.by_id[class_idref].name
            for a in c/"attribute":
                props = classifications[class_name].get("Properties")
                if props is None:
                    props = classifications[class_name]["Properties"] = []
                props.append(a.name)

    class_names = sorted(classifications.keys())
    annotated = set()
    
    def annotate_parent(cn):      
        if cn in annotated: return
        annotated.add(cn)
        node = class_name_to_node.get(cn)
        try:
            for rel in (node|"links")/"Generalization":
                if rel.start == node.idref:
                    pc = xmi_doc.by_id[rel.end]
                    classifications[cn]["Parent"] = pc.name
                    annotate_parent(pc.name)
        except ValueError as e:
            print(e, file=sys.stderr)
                
                
    # import pdb; pdb.set_trace()
    for cn in class_names:
        annotate_parent(cn)
        
    return data
        

json.dump(generate_definitions(), OUTPUT, indent=2)
