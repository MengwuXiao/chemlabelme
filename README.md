# ChemLabelMe

ChemLabelMe is a tool used for annotating and correcting the correspondence between chemical structures and chemical information (ID, chemical name, properties) in papers/patents, and has been used to assist in manual correction of the CarsiChemIE dataset (https://github.com/carbonsilicon-ai/CarsiChemIE ). This software is modified based on LabelMe (https://github.com/wkentaro/labelme ). After modifying the code, the following functions were mainly added: displaying annotation box IDs, displaying IDs in the label bar, indentation of non chemical structure labels in the label bar, double-click annotation boxes to achieve quick matching of chemical structure labels (1) with other labels, adding prompt windows, etc. Compared to LabelMe, the modified software can improve the accuracy and efficiency of manual correction of corresponding relationships.

 ![screenshot of the ChemLabelMe](image/example.jpg "screenshot of the ChemLabelMe")


# example video
https://mwxiao.com/chemlabelme/chemlabelme.mp4  


# Usage   
## step 1  
```
conda create -n py38 python=3.8  
conda activate py38  
pip install labelme  
```  

## step 2  
Find the labelme folder (path to Anaconda3\envs\py38\Lib\site-packages\labelme), delete all files inside, and copy this code to that folder.  

## step 3  
run modified Labelme using Anaconda Prompt.   
```   
conda activate py38  
labelme   
```  


---  
# Chinese version of README   

ChemLabelMe是一个用于标注和校正论文/专利中化学结构与化学信息（编号、化学名、性质等）对应关系的小工具，已用于辅助CarsiChemIE数据集的人工校正（https://github.com/carbonsilicon-ai/CarsiChemIE ）。 本软件是基于LabelMe（https://github.com/wkentaro/labelme ）修改的，修改代码后，主要增加以下功能：显示标注框ID、标签栏显示ID、非化学结构标签在标签栏缩进、双击标注框实现化学结构标签（1）与其他标签的快速匹配、增加提示窗口等。 相对于LabelMe，修改后的软件可以提高人工校正对应关系的准确性和效率。

# 实例视频  
https://mwxiao.com/chemlabelme/chemlabelme.mp4  


# 用法  
## 步骤一  
创建Python 3.8环境，并安装labelme。 注：Python 3.10暂时会报错。  
```
conda create -n py38 python=3.8  
conda activate py38  
pip install labelme  
```  

## 步骤二  
找到LabelMe文件夹 (一般在Anaconda3\envs\py38\Lib\site-packages\labelme)，删除该文件夹所有文件，将本项目代码复制到该文件夹。  

## 步骤三   
通过Anaconda Prompt运行修改后的LabelMe。    
```   
conda activate py38  
labelme   
```   
