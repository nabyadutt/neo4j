{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "eac21a4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting neo4j\n",
      "  Downloading neo4j-5.8.0.tar.gz (187 kB)\n",
      "     -------------------------------------- 187.5/187.5 kB 3.8 MB/s eta 0:00:00\n",
      "  Installing build dependencies: started\n",
      "  Installing build dependencies: finished with status 'done'\n",
      "  Getting requirements to build wheel: started\n",
      "  Getting requirements to build wheel: finished with status 'done'\n",
      "  Installing backend dependencies: started\n",
      "  Installing backend dependencies: finished with status 'done'\n",
      "  Preparing metadata (pyproject.toml): started\n",
      "  Preparing metadata (pyproject.toml): finished with status 'done'\n",
      "Requirement already satisfied: pytz in c:\\users\\kushagra\\anaconda3\\lib\\site-packages (from neo4j) (2022.1)\n",
      "Building wheels for collected packages: neo4j\n",
      "  Building wheel for neo4j (pyproject.toml): started\n",
      "  Building wheel for neo4j (pyproject.toml): finished with status 'done'\n",
      "  Created wheel for neo4j: filename=neo4j-5.8.0-py3-none-any.whl size=258422 sha256=ff0c405e8a110f7bd33bcef00f87204718a5cded19ae35cf4d037d8de813fa53\n",
      "  Stored in directory: c:\\users\\kushagra\\appdata\\local\\pip\\cache\\wheels\\3e\\ef\\4c\\a91599f59166356b3942580360be2362563a7a97c877d018ca\n",
      "Successfully built neo4j\n",
      "Installing collected packages: neo4j\n",
      "Successfully installed neo4j-5.8.0\n"
     ]
    }
   ],
   "source": [
    "!pip install neo4j"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "459f69a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from neo4j import GraphDatabase\n",
    "gdb = GraphDatabase.driver(uri='bolt://localhost:7687',auth=(\"neo4j\",\"12345678\"))\n",
    "se = gdb.session()\n",
    "q1 = '''create (JubinNautiyal:professor:associate:male:law{name:\"Jubin Nautiyal\",age:32,state:\"Rajasthan\",mode:\"Hybrid\"})'''\n",
    "nodes = se.run(q1)\n",
    "for node in nodes:\n",
    "    print(node)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3909c73e",
   "metadata": {},
   "outputs": [],
   "source": [
    "q2 = '''create (RochakKohli:professor:senior:male:computerscience{name:\"Rochak Kohli\",age:40,state:\"Noida\",mode:\"Hybrid\"})'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b687a791",
   "metadata": {},
   "outputs": [],
   "source": [
    "nodes = se.run(q2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "341418cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<neo4j._sync.work.result.Result at 0x1457ac08880>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "q3 = '''create (LataMangeshkar:professor:senior:female:law{name:\"Lata Mangeshkar\",age:60,state:\"Bihar\",mode:\"Online\"})'''\n",
    "se.run(q3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba698aa8",
   "metadata": {},
   "source": [
    "create (MitraSingh:professor:senior:female:computerscience{name:\"Mitra Singh\",age:37,state:\"Uttarakhand\",mode:\"Offline\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "707ba3b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "q3 = '''create (LataMangeshkar:professor:senior:female:law{name:\"Lata Mangeshkar\",age:60,state:\"Bihar\",mode:\"Online\"})'''\n",
    "q4 = '''create (KishoreKumar:professor:associate:male:bussiness{name:\"Kishore Kumar\",age:45,state:\"Jammu and Kashmir\",mode:\"Offline\"})'''\n",
    "q5 = '''create (NeerajSridhar:professor:junior:male:law{name:\"Neeraj Sridhar\",age:31,state:\"Mumbai\",mode:\"Offline\"})'''\n",
    "q6 = '''create (ArmaanMalik:professor:junior:male:computerscience{name:\"Armaan Malik\",age:25,state:\"Delhi\",mode:\"Online\"})'''\n",
    "q7 = '''create (DiljitDosanjh:professor:junior:male:bussiness{name:\"Diljit Dosanjh\",age:32,state:\"Chandigarh\",mode:\"Offline\"})'''\n",
    "q8 = '''create (ArijitSingh:professor:associate:male:law{name:\"Arijit Singh\",age:42,state:\"Hyderabad\",mode:\"Hybrid\"})'''\n",
    "q9 = '''create (NehaKakkar:professor:junior:female:computerscience{name:\"Neha Kakkar\",age:37,state:\"Delhi\",mode:\"Offline\"})'''\n",
    "q10 = '''create (SukritiKakkar:professor:junior:female:bussiness{name:\"Sukriti Kakkar\",age:35,state:\"Bihar\",mode:\"Online\"})'''\n",
    "q11 = '''create (AshaBhosle:professor:senior:female:computerscience{name:\"Asha Bhosle\",age:68,state:\"Tamil Nadu\",mode:\"Offline\"})'''\n",
    "q12 = '''create (AnneMarie:professor:associate:female:law{name:\"Anne Marie\",age:32,state:\"Los Angeles\",mode:\"Online\"})'''\n",
    "q13 = '''create (HoneySingh:professor:associate:male:computerscience{name:\"Honey Singh\",age:42,state:\"Odissa\",mode:\"Offline\"})'''\n",
    "q14 = '''create (AtifAslam:professor:junior:male:bussiness{name:\"Atif Aslam\",age:36,state:\"Karachi\",mode:\"Hybrid\"})'''\n",
    "q15 = '''create (ShreyaGhoshal:professor:senior:female:computerscience{name:\"Shreya Ghoshal\",age:47,state:\"Uttar Pradesh\",mode:\"Offline\"})'''\n",
    "q16 = '''create (SunidhiChauhan:professor:senior:female:bussiness{name:\"Sunidhi Chauhan\",age:45,state:\"Gujrat\",mode:\"Online\"})'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a92d37be",
   "metadata": {},
   "source": [
    "admin, access_denied, viewer, editor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "600a93c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<neo4j._sync.work.result.Result at 0x1456761b340>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "se.run(q4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "608cb0c2",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<neo4j._sync.work.result.Result at 0x14579c0c310>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "se.run(q5)\n",
    "se.run(q6)\n",
    "se.run(q7)\n",
    "se.run(q8)\n",
    "se.run(q9)\n",
    "se.run(q10)\n",
    "se.run(q11)\n",
    "se.run(q12)\n",
    "se.run(q13)\n",
    "se.run(q14)\n",
    "se.run(q15)\n",
    "se.run(q16)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "bd844ad7",
   "metadata": {},
   "outputs": [],
   "source": [
    "qq1 = '''create (RECORDS:department{dept:'Records'})'''\n",
    "qq2 = '''create (ADMISSIONS:department{dept:'Admissions'})'''\n",
    "qq3 = '''create (EXAMINATIONS:department{dept:'Examinations'})'''\n",
    "qq4 = '''create (EVENTS:department{dept:'Events'})'''\n",
    "qq5 = '''create (DISCIPLINE:department{dept:'Discipline'})'''\n",
    "qq6 = '''create (IT:department{dept:'IT'})'''\n",
    "qq7 = '''create (OPERATIONS:department{dept:'Operations'})'''\n",
    "qq8 = '''create (LOGISTIC:department{dept:'Logistic'})'''\n",
    "qq9 = '''create (CULTURAL:department{dept:'Cultural'})'''\n",
    "qq10 = '''create (ATTENDANCE:department{dept:'Attendance'})'''\n",
    "qq11 = '''create (EXTRACURRICULAR:department{dept:'Extracurriculars'})'''\n",
    "qq12 = '''create (HUMANRESOURCES:department{dept:'Human Resources'})'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "ee0a96b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<neo4j._sync.work.result.Result at 0x14579b060a0>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "se.run(qq1)\n",
    "se.run(qq2)\n",
    "se.run(qq3)\n",
    "se.run(qq4)\n",
    "se.run(qq5)\n",
    "se.run(qq6)\n",
    "se.run(qq7)\n",
    "se.run(qq8)\n",
    "se.run(qq9)\n",
    "se.run(qq10)\n",
    "se.run(qq11)\n",
    "se.run(qq12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "272169d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "gururandhawa_r = ['''MATCH (a:junior), (b:department) where a.name='Guru Randhawa' AND b.dept='Records' CREATE (a)-[r1:viewer]->(b) return r1''',\n",
    "   '''MATCH (a:junior), (b:department) where a.name='Guru Randhawa' AND b.dept='Finance' CREATE (a)-[r2:access_denied]->(b) return r2''',\n",
    "   '''MATCH (a:junior), (b:department) where a.name='Guru Randhawa' AND b.dept='Examinations' CREATE (a)-[r3:viewer]->(b) return r3''',\n",
    "   '''MATCH (a:junior), (b:department) where a.name='Guru Randhawa' AND b.dept='Events' CREATE (a)-[r4:editor]->(b) return r4''',\n",
    "   '''MATCH (a:junior), (b:department) where a.name='Guru Randhawa' AND b.dept='Discipline' CREATE (a)-[r5:viewer]->(b) return r5''',\n",
    "   '''MATCH (a:junior), (b:department) where a.name='Guru Randhawa' AND b.dept='IT' CREATE (a)-[r6:access_denied]->(b) return r6''',\n",
    "   '''MATCH (a:junior), (b:department) where a.name='Guru Randhawa' AND b.dept='Operations' CREATE (a)-[r7:acess_denied]->(b) return r7''',\n",
    "   '''MATCH (a:junior), (b:department) where a.name='Guru Randhawa' AND b.dept='Logistic' CREATE (a)-[r8:access_denied]->(b) return r8''',\n",
    "   '''MATCH (a:junior), (b:department) where a.name='Guru Randhawa' AND b.dept='Cultural' CREATE (a)-[r9:viewer]->(b) return r9''',\n",
    "   '''MATCH (a:junior), (b:department) where a.name='Guru Randhawa' AND b.dept='Attendance' CREATE (a)-[r10:editor]->(b) return r10''',\n",
    "   '''MATCH (a:junior), (b:department) where a.name='Guru Randhawa' AND b.dept='Extracurriculars' CREATE (a)-[r11:editor]->(b) return r11''',\n",
    "   '''MATCH (a:junior), (b:department) where a.name='Guru Randhawa' AND b.dept='Human Resources' CREATE (a)-[r12:viewer]->(b) return r12''']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b74bf079",
   "metadata": {},
   "outputs": [],
   "source": [
    "for r in gururandhawa_r:\n",
    "    se.run(r)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a58cfc13",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}