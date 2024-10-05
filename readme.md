# SeMMed - Neo4j Project

## Table of Contents
1. [Overview](#overview)
2. [Objective](#objective)
3. [Use](#use)
4. [Important References](#important-references)


## Overview

This project was completed as a capstone project for Big Data course I took during my undergraduate studies.

The professor of the course, Dr. Fitzroy Nembhard, proposed that using a graph-based database like Neo4j would allow use to relate the largely decoupled [National Library of Medicine's Semantic Medline Database](https://lhncbc.nlm.nih.gov/ii/tools/SemRep_SemMedDB_SKR.html).

"The Semantic MEDLINE Database (SemMedDB) is a repository of semantic predications (subject-predicate-object triples) extracted by SemRep, a semantic interpreter of biomedical text. SemMedDB currently contains information about approximately 96.3 million predications from all of PubMed citations (about 29.1 million citations) and forms the backbone of the Semantic MEDLINE application." Taken from directly from linked site.

At the completion of this project, we aimed to prove that we could create more intuitive and useful version database using all of the information spread across the current "database" using a graph representation.

The project included basic data cleaning processes, AWS data storage/retrieval, Neo4j Database querying, and some performance analysis.

The research and development team was comprised of 7 people and ended in December 2023:

    - Thu Thu Hlaing
    - Aristotelis Dougales
    - Dhruthi Sridhar Murthy
    - Ali Barfi Bafghi
    - Joshua Breininger
    - Candice Normalee Chambers
    - Malakai Spann

While the project presentation was completed in equal parts by all team members, I designed and tested all parts of the development effort.

## Objective

To explore ways in which we can use knowledge graphs via Neo4J to display the biomedical concepts found within the [Semantic Medline Database](https://lhncbc.nlm.nih.gov/ii/tools/SemRep_SemMedDB_SKR.html) and their relationships.

## Use 

This project is not intended to be used as a template or guide, but it can definitely can be used as "inspiration." Please link back to [this repo](https://github.com/KayDVC/semmed-neo4j) or [my website](https://www.malakaispann.com) if you do.


## Final Notes
Though the project was completed around December of 2023, it took me quite a while to get back around to cleaning up the various files to be uploaded to Github.

In preparation for upload, I went back and verified that all of the packages used during the original development effort were still available. Due to this, I needed to update quite a few packages and re-run some code cells to display the updated information.

Also, we only had access to the reference AWS resources over the duration of the course. After it ended, our accounts and all associated data were erased.

Lastly, as references multiple times in `neo4j/results_final.ipynb`, this project was ultimately a proof-of-concept which introduced some restrictions in our efforts. One of these was the inability test our Neo4j relational logic on all of the data from the original database.

Thanks, 

\- Kay


