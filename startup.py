import dashboard
import FastAPI
import multiprocessing
jobs = []
jobs.append(multiprocessing.Process(target=FastAPI.start))
jobs.append(multiprocessing.Process(target=dashboard.start))

for j in jobs:
    j.start()
