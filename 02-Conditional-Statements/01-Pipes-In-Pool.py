pool_vol = int(input())
pipe_1_flow = int(input())
pipe_2_flow = int(input())
hours = float(input())

pipe_1_result = pipe_1_flow * hours
pipe_2_result = pipe_2_flow * hours

total = pipe_1_result + pipe_2_result

if total <= pool_vol:
    pool_fullness = total / pool_vol
    pipe_1_percent = pipe_1_result / total
    pipe_2_percent = pipe_2_result / total

    print(f"The pool is {pool_fullness :.2%} full. "
          f"Pipe 1: {pipe_1_percent :.2%}. "
          f"Pipe 2: {pipe_2_percent :.2%}.")
else:
    print(f"For {hours} hours the pool overflows with {total - pool_vol:.2f} liters.")