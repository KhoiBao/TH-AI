import numpy as np # thư viện tính toán toán học
import matplotlib.pyplot as plt # visualize data sử dụng đồ thị
from scipy.spatial.distance import cdist # Hỗ trợ tính khoảng cách


means = [[2, 2], [9, 2], [4, 9]]
cov = [[2, 0], [0, 2]]
n_samples = 500 # Tạo 500 mẫu
n_cluster = 3 # tạo 3 trung tâm
X0 = np.random.multivariate_normal(means[0], cov, n_samples)
X1 = np.random.multivariate_normal(means[1], cov, n_samples)
X2 = np.random.multivariate_normal(means[2], cov, n_samples)
X = np.concatenate((X0, X1, X2), axis = 0)

plt.xlabel("x")
plt.ylabel("y")
plt.plot(X[:, 0], X[:, 1], "bo", markersize=5)

#plt.plot()
#plt.show()

#Khởi tạo tâm cụm 0 với số n_cluster = 3
def kmeans_init_centers(X, n_cluster):
    return X[np.random.choice(X.shape[0], n_cluster, replace=False)]

#Hàm tính toán của Kmeans thông qua thư viện cdist để xác định tâm cụm
def kmeans_predict_labels(X, centers):
    D = cdist(X, centers)
# return index of the closest center
    return np.argmin(D, axis = 1)

# hàm cập nhật vị trí gần tâm cụm
def kmeans_update_centers(X, labels, n_cluster):
    centers = np.zeros((n_cluster, X.shape[1]))
    for k in range(n_cluster):
        # collect all points assigned to the k-th cluster
        Xk = X[labels == k, :]
# take average
        centers[k,:] = np.mean(Xk, axis = 0)
    return centers

#Hàm kiểm tra tính hội tụ
def kmeans_has_converged(centers, new_centers):
    # return True if two sets of centers are the same
    return (set([tuple(a) for a in centers]) == set([tuple(a) for a in new_centers]))

#Vẽ đồ thị để xem kết quả

# Hàm này dùng để vẽ dữ liệu lên đồ thị
# Random color chỉ làm việc với k > 4
def kmeans_visualize(X, centers, labels, n_cluster, title):
    plt.xlabel('x')          # label trục x
    plt.ylabel('y')          # label trục y
    plt.title(title)         # title của đồ thị

    plt_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']  # danh sách màu

    for i in range(n_cluster):
        data = X[labels == i]  # lấy dữ liệu của cụm i

        # Vẽ các điểm trong cụm
        plt.plot(
            data[:, 0],
            data[:, 1],
            plt_colors[i] + '^',
            markersize=4,
            label='cluster_' + str(i)
        )

        # Vẽ tâm cụm
        plt.plot(
            centers[i][0],
            centers[i][1],
            plt_colors[i + 4] + 'o',
            markersize=10,
            label='center_' + str(i)
        )

    plt.legend()  # Hiện bảng chú thích
    plt.show()

# KMeans algorithm
def kmeans(init_centers, init_labels, X, n_cluster):
    centers = init_centers
    labels = init_labels
    times = 0

    while True:
        # Gán nhãn
        labels = kmeans_predict_labels(X, centers)
        kmeans_visualize(
            X, centers, labels, n_cluster,
            'Assigned label for data at time = ' + str(times + 1)
        )

        # Cập nhật tâm cụm
        new_centers = kmeans_update_centers(X, labels, n_cluster)

        # Kiểm tra hội tụ
        if kmeans_has_converged(centers, new_centers):
            break

        centers = new_centers
        kmeans_visualize(
            X, centers, labels, n_cluster,
            'Update center position at time = ' + str(times + 1)
        )

        times += 1

    return centers, labels, times

# Chạy KMean
init_centers = kmeans_init_centers(X, n_cluster)
print(init_centers)  # Tọa độ tâm cụm ban đầu

init_labels = np.zeros(X.shape[0])

kmeans_visualize(
    X, init_centers, init_labels, n_cluster,
    'Init centers in the first run. Assigned all data as cluster 0'
)

centers, labels, times = kmeans(init_centers, init_labels, X, n_cluster)

print('Done! KMeans has converged after', times, 'times')
print(centers)

