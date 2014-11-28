

def compute_fundamental(x1, x2):

  n = x1.shape[1]
  if x2.shape[1] != n:
    raise ValueError("Number of points don't match")

  # build a matrix for equations
  A = zeros(n,9)
  for i in range(n):
    A[i] = [x1[0,i]*x2[0,i],
        x1[0,i]*x2[1,i],
        x1[0,i]*x2[2,i],
        x1[1,i]*x2[0,i],
        x1[1,i]*x2[1,i],
        x1[1,i]*x2[2,i],
        x1[2,i]*x2[0,i],
        x1[2,i]*x2[1,i],
         x1[2,i]*x2[2,i] ]

