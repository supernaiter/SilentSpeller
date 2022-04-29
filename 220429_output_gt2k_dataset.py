# %%
# import
import csv
import os
import pickle

import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA

from tqdm import tqdm


#%%
npz = np.load("p1_old_dataset.npz", allow_pickle=True)
print(npz.files)

print(npz["label"])
print(len(npz["label"]))
print(len(npz["data"]))


# %%
# Making data without PCA.
# 書き込み
folder_path = "gt2k_raw"
visualization_path = "gt2k_raw_visualization"
try:
    os.mkdir(folder_path)
except:
    pass

#try:
#    os.mkdir(visualization_path)
# except:
#    pass


try:
    os.mkdir(folder_path + "/data")
    os.mkdir(folder_path + "/label")

except:
    pass

count = 0
for i in tqdm(range(len(npz["label"]))):
    smartpalate_data = npz["data"][i]
    script = npz["label"][i].lower()

    # smartpalate_data = [[float(y) for y in x] for x in [row[0] for row in smartpalate_data]]
    # fig = plt.figure()
    # plt.xlim([0,500])
    data_frames_np = np.array(smartpalate_data)
    # im = plt.imshow(data_frames_np.T)
    scaled_data_frames_np = data_frames_np
    # plt.show()
    # print(scaled_data_frames_np.shape)

    filename = str(i) + script

    try:
        # plt.savefig(visualization_path + "/" +str(filename) +".png")
        outF = open(folder_path + "/data/" + str(filename), "w")

        for line in scaled_data_frames_np:
            outF.write(str(list(line)).strip("[]").replace(",", " "))
            outF.write("\n")
        outF.close()

        # write label
        label = open(folder_path + "/label/" + str(filename) + ".lab", "w")
        test_line = script.split()

        label.write("sil" + "\n")
        # for i in test_line:
        for countt, scr in enumerate(test_line):

            if countt == len(test_line) - 1:
                for j in list(scr):
                    label.write(j + "\n")
                break

            else:
                for j in list(scr):
                    label.write(j + "\n")
                label.write("_" + "\n")

        label.write("sil")
        label.close()
        count += 1

    except Exception as e:
        print(e)
# %% making PCA


def make_pca_model(data, dimentions):
    # dataはnumpy?
    pca = PCA(n_components=dimentions)
    pca.fit(data)

    print(pca.explained_variance_ratio_)

    return pca


# Load the data and concatenate them as "data."
# This process is needed to make PCA model.
data = []

for sample in npz["data"]:
    data.extend(sample)

data_frames_np = np.array(data)
print(data_frames_np.shape)


# %%
# You can add the different dimensions like:
# for pca_dimention in [4,8,16, 32]:
for pca_dimention in [16]:
    pca = make_pca_model(data_frames_np, pca_dimention)
    pickle.dump(pca, open(str(pca_dimention) + "pca.pkl", "wb"))
    reduced_all_data_frames_np = pca.transform(data_frames_np)

    features_mmscaler = preprocessing.MinMaxScaler()  # インスタンスの作
    features_mmscaler.fit(reduced_all_data_frames_np)

    pickle.dump(features_mmscaler, open(str(pca_dimention) + "mmscaler.pkl", "wb"))

    # 書き込み
    folder_path = "gt2k_2328_" + str(pca_dimention)

    try:
        os.mkdir(folder_path)
    except:
        pass
    try:
        os.mkdir(folder_path + "/data")
        os.mkdir(folder_path + "/label")

    except:
        pass

    count = 0
    for i in tqdm(range(len(npz["label"]))):
        smartpalate_data = npz["data"][i]
        script = npz["label"][i].lower()

        data_frames_np = np.array(smartpalate_data)
        scaled_data_frames_np = features_mmscaler.transform(
            pca.transform(data_frames_np)
        )

        filename = str(i) + script

        try:
            outF = open(folder_path + "/data/" + str(filename), "w")

            for line in scaled_data_frames_np:
                outF.write(str(list(line)).strip("[]").replace(",", " "))
                outF.write("\n")
            outF.close()

            # write label
            label = open(folder_path + "/label/" + str(filename) + ".lab", "w")
            test_line = script.split()

            label.write("sil" + "\n")
            # for i in test_line:
            for countt, scr in enumerate(test_line):

                if countt == len(test_line) - 1:
                    for j in list(scr):
                        label.write(j + "\n")
                    break

                else:
                    for j in list(scr):
                        label.write(j + "\n")
                    label.write("_" + "\n")

            label.write("sil")
            label.close()
            count += 1

        except Exception as e:
            print(e)
