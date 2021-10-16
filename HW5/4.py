# import random

# def run_ransac(data, estimate, is_inlier, sample_size, goal_inliers, max_iterations, stop_at_goal=True):
#     best_ic = 0
#     best_model = None


#     data = list(data)
#     for i in range(max_iterations):
#         s = random.sample(data, int(sample_size))
#         m = estimate(s)
#         ic = 0
#         for j in range(len(data)):
#             if is_inlier(m, data[j]):
#                 ic += 1

#         if ic > best_ic:
#             best_ic = ic
#             best_model = m
#             if ic > goal_inliers and stop_at_goal:
#                 break
#     return best_model, best_ic

# def augment(xys):
#     axy = np.ones((len(xys), 3))
#     axy[:, :2] = xys
#     return axy


# def estimate(xys):
#     axy = augment(xys[:2])
#     return np.linalg.svd(axy)[-1][-1, :]


# def is_inlier(coeffs, xy, threshold):
#     return np.abs(coeffs.dot(augment([xy]).T)) < threshold

def ransac(image):
    img = image.copy()
    # import matplotlib
    # import matplotlib.pyplot as plt

    n = 100
    max_iterations = 100
    goal_inliers = n * 0.3

    xys = np.random.random((n, 2)) * 10
    xys[:50, 1:] = xys[:50, :1]

    # plt.scatter(xys.T[0], xys.T[1])

    m, b = run_ransac(xys, estimate, lambda x, y: is_inlier(
        x, y, 0.01), goal_inliers, max_iterations, 20)
    a, b, c = m
    # plt.plot([0, 10], [-c/b, -(c+10*a)/b], color=(0, 1, 0))

    # plt.show()

    return rho, theta

