#===创建的目录= 函数===#
def mkdir(path):
    import os      # 引入模块
    isExists=os.path.exists(path) # 判断路径是否存在 #存在True  #不存在 False
    if not isExists: # 判断结果
        os.makedirs(path) # 创建目录操作函数
        print (path +' 创建成功')
        return True
    else:  
        print (path+' 目录已存在')# 如果目录存在则不创建，并提示目录已存在
        return False

if True:
    # 定义要创建的目录2
    Image_path2 = ["./Train_weight_save/HLG_Ori_weight/Ori_res50_weight",  "./Train_weight_save/HLG_Ori_weight/Ori_vgg16_weight", "./Train_weight_save/HLG_Ori_weight/Ori_mobv3_weight",
                "./Train_weight_save/HLG_Rb_weight/Rb_res50_weight",  "./Train_weight_save/HLG_Rb_weight/Rb_vgg16_weight", "./Train_weight_save/HLG_Rb_weight/Rb_mobv3_weight"]   
    # 调用函数2
    for path in Image_path2:
        mkdir(path)
