def schedule_with_deadline(jobs):
    # Sort the array of jobs based on profit in non-decreasing order
    jobs.sort(key=lambda job: job['profit'])

    n = len(jobs)
    i = 0
    schedule = []

    while i < n:
        # Select the next job i from the sorted list
        job_i = jobs[i]

        # Scheduling job is feasible if it doesn't conflict with the current schedule
        if is_feasible(schedule, job_i):
            schedule.append(job_i)
        
        i += 1

    return schedule

def is_feasible(schedule, job_i):
    # Check feasibility by making sure the job's deadline isn't exceeded
    if not schedule:
        return True
    last_job = schedule[-1]
    return last_job['deadline'] < job_i['deadline']

# Example usage
jobs = [
    {'job_id': 1, 'profit': 30, 'deadline': 3},
    {'job_id': 2, 'profit': 20, 'deadline': 2},
    {'job_id': 3, 'profit': 10, 'deadline': 1},
    {'job_id': 4, 'profit': 40, 'deadline': 4},
]

optimal_schedule = schedule_with_deadline(jobs)
print("Optimal Schedule:", [job['job_id'] for job in optimal_schedule])
