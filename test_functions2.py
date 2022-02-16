from tensorflow.keras.datasets import cifar10
import matplotlib.pyplot as plt
from PIL import Image
import pydicom
import numpy as np
import glob

import CT_MR_utils_opt
import T1_STIR_utils
import T1_STIR_utils_opt
import cyclegan_main
import cyclegan_main_opt
import cyclegan_main_opt_backup


CT_MR_utils_opt.create_hdf5_file_adata('CT', 'MR_T1DUAL_InPhase', num_of_data=20)
cyclegan_main_opt_backup.main('CT', 'MR_T1DUAL_InPhase')





# cyclegan_main.ct_cross_mr('CT', 'MR_T1DUAL_InPhase')

# cifar10 format
# (target_data, _), (test_target_data, _) = cifar10.load_data()
# plt.imshow(target_data[0])
# plt.show()


# Operate on datasets
# CT_MR_utils.load_data("CT", "MR_T1DUAL_InPhase")

# load images T1_STIR
# data = T1_STIR_utils_opt.load_data('T1', 'STIR')
# pass

# show images T1_STIR
# data = T1_STIR_utils.readBinaryData("Data_T1_STIR/bone-marrow-oedema-data/T1/T1_1_400_400_18_2_.raw", 400, 18, 2)
# for i in range(18):
#     toshow = data[:,:,i]
#     plt.imshow(toshow)
#     fig = plt.figure(frameon=False)
#     ax = plt.Axes(fig, [0., 0., 1., 1.])
#     ax.set_axis_off()
#     fig.add_axes(ax)
#     ax.imshow(toshow, aspect='auto') #, cmap=plt.cm.bone)
# plt.show()
# pass



# # show images
# img = pydicom.dcmread("CT_MR/Data_CT_MR/CT/1/DICOM_anon/i0000,0000b.dcm")
# img_array = img.pixel_array
# # plt.imshow(img_array) #, cmap=plt.cm.bone)
# # plt.show()
# fig = plt.figure(frameon=False)
# # fig.set_size_inches(w,h)
# ax = plt.Axes(fig, [0., 0., 1., 1.])
# ax.set_axis_off()
# fig.add_axes(ax)
# ax.imshow(img_array, aspect='auto') #, cmap=plt.cm.bone)
# fig.savefig('Do wysłania/przyklad_jasne.png') #, dpi)
# plt.show()


# img = pydicom.dcmread("Data_CT_MR/CT/4/DICOM_anon/i0000,0000b.dcm")
# img_array = img.pixel_array
# # plt.imshow(img_array) #, cmap=plt.cm.bone)
# # plt.show()
# fig = plt.figure(frameon=False)
# # fig.set_size_inches(w,h)
# ax = plt.Axes(fig, [0., 0., 1., 1.])
# ax.set_axis_off()
# fig.add_axes(ax)
# ax.imshow(img_array, aspect='auto') #, cmap=plt.cm.bone)
# fig.savefig('Do wysłania/przyklad_ciemne.png') #, dpi)
# plt.show()

# # Operacje na CT
# all_source = []
# # #trash
# # img_size = [0, 0]
# # change_ctr = -1
#
# for folder_num in range(1, 41):
#     files = sorted(glob.glob("Data_CT_MR/CT/" + str(folder_num) + "/DICOM_anon/*.dcm"))  # get all the .dcm files from folder
#     counter = 0
#     for file in files:  # iterate over the list of files
#         # print(counter)
#         # read and append to array (funkcja 1)
#         img = pydicom.dcmread(file)
#         img_array = img.pixel_array
#
#         # #trash
#         # if not img_size == img_array.shape:
#         #     img_size = img_array.shape
#         #     change_ctr += 1
#
#         all_source.append(img_array)
#
#         # # save to folder (funkcja 2)
#         # fig = plt.figure(frameon=False)
#         # # fig.set_size_inches(w,h)
#         # ax = plt.Axes(fig, [0., 0., 1., 1.])
#         # ax.set_axis_off()
#         # fig.add_axes(ax)
#         # ax.imshow(img_array, aspect='auto')
#         # fig.savefig('Data_CT_MR/CT/all_pyplot/' + str(folder_num) + '_' + str(counter)) #, dpi)
#         # counter += 1
# plt.show()
# all_source = np.array(all_source)
# # print(change_ctr)
# # print(img_size)


# # Operacje na MR - T1DUAL In Phase
# all_source = []
#
# #trash
# img_size = [0, 0]
# change_ctr = -1
#
# for folder_num in range(1, 41):
#     files = sorted(glob.glob("Data_CT_MR/MR/" + str(folder_num) + "/T1DUAL/DICOM_anon/InPhase/*.dcm"))  # get all the .dcm files from folder
#     counter = 0
#     for file in files:  # iterate over the list of files
#         # read and append to array (funkcja 1)
#         img = pydicom.dcmread(file)
#         img_array = img.pixel_array
#         all_source.append(img_array)
#
#         #trash
#         if not img_size == img_array.shape:
#             img_size = img_array.shape
#             change_ctr += 1
#
#         # save to folder (funkcja 2)
#         fig = plt.figure(frameon=False)
#         # fig.set_size_inches(w,h)
#         ax = plt.Axes(fig, [0., 0., 1., 1.])
#         ax.set_axis_off()
#         fig.add_axes(ax)
#         ax.imshow(img_array, aspect='auto')
#         fig.savefig('Data_CT_MR/MR/all_pyplot/T1DUAL/InPhase/' + str(folder_num) + '_' + str(counter)) #, dpi)
#         counter += 1
# # plt.show()
# all_source = np.array(all_source)
#
# print(change_ctr)
# print(img_size)



# # Operacje na MR - T1DUAL Out Phase
# all_source = []
#
# #trash
# img_size = [0, 0]
# change_ctr = -1
#
# for folder_num in range(1, 41):
#     files = sorted(glob.glob("Data_CT_MR/MR/" + str(folder_num) + "/T1DUAL/DICOM_anon/OutPhase/*.dcm"))  # get all the .dcm files from folder
#     counter = 0
#     for file in files:  # iterate over the list of files
#         # read and append to array (funkcja 1)
#         img = pydicom.dcmread(file)
#         img_array = img.pixel_array
#         all_source.append(img_array)
#
#         #trash
#         if not img_size == img_array.shape:
#             img_size = img_array.shape
#             change_ctr += 1
#
#         # save to folder (funkcja 2)
#         fig = plt.figure(frameon=False)
#         # fig.set_size_inches(w,h)
#         ax = plt.Axes(fig, [0., 0., 1., 1.])
#         ax.set_axis_off()
#         fig.add_axes(ax)
#         ax.imshow(img_array, aspect='auto')
#         fig.savefig('Data_CT_MR/MR/all_pyplot/T1DUAL/OutPhase/' + str(folder_num) + '_' + str(counter)) #, dpi)
#         counter += 1
# # plt.show()
# all_source = np.array(all_source)
#
# print(change_ctr)
# print(img_size)



# # Operacje na MR - T2SPIR
# all_source = []
#
# #trash
# img_size = [0, 0]
# change_ctr = -1
#
# for folder_num in range(1, 41):
#     files = sorted(glob.glob("Data_CT_MR/MR/" + str(folder_num) + "/T2SPIR/DICOM_anon/*.dcm"))  # get all the .dcm files from folder
#     counter = 0
#     for file in files:  # iterate over the list of files
#         # read and append to array (funkcja 1)
#         img = pydicom.dcmread(file)
#         img_array = img.pixel_array
#         all_source.append(img_array)
#
#         #trash
#         if not img_size == img_array.shape:
#             img_size = img_array.shape
#             change_ctr += 1
#
#         # save to folder (funkcja 2)
#         fig = plt.figure(frameon=False)
#         # fig.set_size_inches(w,h)
#         ax = plt.Axes(fig, [0., 0., 1., 1.])
#         ax.set_axis_off()
#         fig.add_axes(ax)
#         ax.imshow(img_array, aspect='auto')
#         fig.savefig('Data_CT_MR/MR/all_pyplot/T2SPIR/' + str(folder_num) + '_' + str(counter)) #, dpi)
#         counter += 1
# # plt.show()
# all_source = np.array(all_source)

# print(change_ctr)
# print(img_size)
# pass
