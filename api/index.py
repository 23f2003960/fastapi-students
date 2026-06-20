from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import csv, os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

students = []
csv_path = os.path.join(os.path.dirname(__file__), '..', 'q-fastapi.csv')
with open(csv_path, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append({"studentId": int(row["studentId"]), "class": row["class"]})

@app.get("/api")
def get_students(class_: List[str] = Query(default=[], alias="class")):
    if not class_:
        return {"students": students}
    filtered = [s for s in students if s["class"] in class_]
    return {"students": filtered}
