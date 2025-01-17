# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:38:27 2021

@author: jbren
"""

from SKEMPI import skempi_final as db
import numpy as np
import protein
import re

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s [%(asctime)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

PDB_Loc="data/raw/PDBs"
fasta_Loc='data/seq'
fasta_db_loc='data/db/Pfam-A.fasta'
    
# Use this function to loop over the entire protein complex
def loop_over_proteins (db):
    # Returns an array of the protein codes
    pdbs= db['#Pdb'].str.slice(start=0, stop=4, step=1)
    # Returns only the unique values from the array
    uniq_pdbs=pdbs.unique()
    i=0
    p=protein.ProteinMethods(PDB_Loc)
    while i<10: #len(uniq_pdbs):
        i+=1
        
# Use this function to loop over the chains within a PDB   
def loop_over_chains (db):
    # Returns only the unique values from the the three columns selected
    # see https://stackoverflow.com/questions/26977076/pandas-unique-values-multiple-columns 
    # for diffent ways to do this
    uniq_chains=np.unique(db[['#Pdb', 'Prot1Chain','Prot2Chain']])
    
    # This function returns all the unique PDB and chain combinations from #PDB but also some of the chains by themselves
    # Next two lines strip out the chain orphan values ie ['A'] and not ['1ACB_A_B']
    selection = np.array([bool(re.search("^\d", element)) for element in uniq_chains])    
    # Apply Boolean mask
    uniq_chains=uniq_chains[selection]
    
    # Returns an array of the protein codes
    uniq_chains_list=np.char.split(uniq_chains.astype(str),'_')
    # Returns an array of the protein codes
    uniq_pdbs=[item[0] for item in uniq_chains_list]
    uniq_Prot1_set=[item[1] for item in uniq_chains_list]  
    uniq_Prot2_set=[item[2] for item in uniq_chains_list]
        
    i=0
    p=protein.ProteinMethods(PDB_Loc)
    #Loop over PDBs and within each PDB over the chains on both sides
    while i<10: #len(uniq_pdbs):
        print(uniq_pdbs[i])
        
        j=0
        while j<len(uniq_Prot1_set[i]):
            # write a fasta sequence file for each chain in the database        
            PDBfile=p.getPDBfile(uniq_pdbs[i])
            #Send the location of the PDB file and the designation of the chain
            seq=p.getSeq(PDBfile,uniq_Prot1_set[i][j])
            fasta_file=p.writeSeq(seq,uniq_pdbs[i],uniq_Prot1_set[i][j],fasta_Loc)
            p.runPSIBlast(fasta_file,fasta_db_loc)
            j+=1
            
        #repeat for the other side of the complex
        k=0
        while k<len(uniq_Prot1_set[i]):     
            PDBfile=p.getPDBfile(uniq_pdbs[i])
            seq=p.getSeq(PDBfile,uniq_Prot1_set[i][k])
            fasta_file=p.writeSeq(seq,uniq_pdbs[i],uniq_Prot1_set[i][k],fasta_Loc)
            p.runPSIBlast(fasta_file,fasta_db_loc)
            k+=1
            
        i+=1
        
# Use this function to loop over each row      
def loop_over_mutations(db):
    pdb=db['#Pdb'].str.slice(start=0, stop=4, step=1) 
    i=0
    while i<10: #len(mutations):
        #dummy placeholder command
        print (str(db.index[i])+"_"+pdb.iloc[i]+"_"+db['Mutation(s)_cleaned'].iloc[i])
        i+=1
# =============================================================================
# Testing        
# =============================================================================
loop_over_proteins(db)
loop_over_chains(db)
# loop_over_mutations(db)
