# Fitch parsimony over the 15 rooted trees (E = outgroup/root).
# Character matrix from morphological observation of the Pokemon guide.
# 0 = Archeops (outgroup/ancestral) state, 1 = derived state.
CHARS = ["streamer_tail","long_neck","webbed_feet","dark_plumage",
         "red_head_ornament","hooked_beak","pointed_wings","crown_crest"]
M = {
 #      1  2  3  4  5  6  7  8
 "E": [0,0,0,0,0,0,0,0],   # Archeops  (outgroup)
 "A": [1,0,0,0,0,0,1,1],   # Articuno
 "B": [0,0,0,1,1,0,1,0],   # Unfezant
 "C": [0,0,0,1,1,1,1,1],   # Staraptor
 "D": [0,1,1,0,0,0,0,0],   # Swanna
}
TREES = {
 1:('E',('A',('B',('C','D')))),
 2:('E',('B',('C',('A','D')))),
 3:('E',('C',('A',('B','D')))),
 4:('E',('D',('A',('B','C')))),
 5:('E',('A',('C',('B','D')))),
 6:('E',('B',('D',('A','C')))),
 7:('E',('C',('D',('A','B')))),
 8:('E',('D',('B',('A','C')))),
 9:('E',('A',('D',('B','C')))),
 10:('E',('B',('A',('C','D')))),
 11:('E',('C',('B',('A','D')))),
 12:('E',('D',('C',('A','B')))),
 13:('E',(('A','C'),('B','D'))),
 14:('E',(('A','B'),('C','D'))),
 15:('E',(('A','D'),('B','C'))),
}
def fitch(node, ci, changes):
    if isinstance(node,str):
        return {M[node][ci]}
    s=[fitch(c,ci,changes) for c in node]
    inter=s[0]&s[1]
    if inter:
        return inter
    changes[0]+=1
    return s[0]|s[1]
def tree_steps(tree):
    per=[]
    for ci in range(len(CHARS)):
        ch=[0]; fitch(tree,ci,ch); per.append(ch[0])
    return sum(per), per

results={}
for t,topo in TREES.items():
    tot,per=tree_steps(topo)
    results[t]=(tot,per)
best=min(v[0] for v in results.values())
print("char order:", CHARS)
print(f"{'Tree':>4} {'steps':>5}  per-character steps")
for t in sorted(results):
    tot,per=results[t]
    star=" <== SHORTEST" if tot==best else ""
    print(f"{t:>4} {tot:>5}  {per}{star}")
print("\nShortest =", best, "steps; trees:", [t for t in results if results[t][0]==best])
# Which characters are homoplastic (>1 step) on the shortest tree(s):
for t in [t for t in results if results[t][0]==best]:
    tot,per=results[t]
    homo=[CHARS[i] for i,s in enumerate(per) if s>1]
    print(f"Tree {t}: homoplastic (convergent) characters:", homo)
