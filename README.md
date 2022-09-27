# Internship_task
## Part1
## Objective
Input a jpg image,run through the YOLOv5 model and get annotations in a XML format.
<summary>Install</summary>
Clone repo and install [requirements.txt](https://github.com/aku134/Internship_task/blob/master/Part1/requirements.txt)
  
```bash
git clone https://github.com/aku134/Internship_task.git  # clone
cd Part1
pip install -r requirements.txt  # install
```


<summary>Run</summary>
Run the following command to get annotations of the image in a XML file.
  
```bash
python detect.py --source data/images/bus.jpg
```
<summary>Output</summary>

The XML file is saved as result_to_xml.xml in the same directory.The image result is saved under runs/detect.