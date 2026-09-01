Open the approx_solution directory in bash and run
./run_test_cases.sh

This will run all of the optimal test cases and print out the time it takes for each test.

With the same directory open in bash, run
./run_nonopt_cases.sh

This will run all of the non-optimal test cases and print out the time it takes for each test.

Test case runtime will not always be consistent because of the use of randomness.

PSEUDOCODE
start = random.paths
while visited < total_vertices:
  if no neighbors found:
    return 0
  next_vertex = random.lowest_candidate
  total_weight = paths[][]
  tour.append(next_vertex)
  currenet = next_vertex
tour.append(start)
return results