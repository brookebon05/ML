from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

digits = load_digits()
# print(digits.DESCR)

print(digits.data[13])  # looking at 13th row, gives pixel intensity 1D
print(digits.data.shape)  # prints (1797, 64) 1797 features
print(digits.target[13])  # prints 3, the target for the 64 bit
print(digits.target.shape)  # prints (1797,) ...each point has one class, one target
print(digits.images[13])  # prints 2D 8x8 array with 64 digits 0-16

figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6, 4))
for item in zip(
    axes.ravel(), digits.images, digits.target
):  # python zip function bundles 3 iterables
    # produces one iterable
    axes, image, target = item  # produces one iterable
    axes.imshow(
        image, cmap=plt.cm.gray_r
    )  # displays multichannel (RGB) or single-channel ("grayscale")
    # image data
    axes.set_xticks([])  # remove x-axis ticks
    axes.set_yticks([])  # remove y-axis ticks
    axes.set_title(target)  # the target value of the image
plt.tight_layout()
# plt.show()

# TRAIN MODEL
data_train, data_test, target_train, target_test = train_test_split(
    digits.data, digits.target, random_state=11
)
# random_state for reproducibility
print(data_train.shape)
print(target_train.shape)
print(data_test.shape)  # (450,64) 25% training 75% testing

knn = KNeighborsClassifier()

# load training data into model using fit method
# Note: KNeighbors classifier does not do calculations, just loads model
knn.fit(X=data_train, y=target_train)
# returns array containing predicted class of each test image

predicted = knn.predict(X=data_test)
# give target value for data set

expected = target_test
print(predicted[:20])
print(expected[:20])
