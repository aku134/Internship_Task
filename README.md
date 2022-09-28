# Internship_task
## Part1
### Objective
Input a jpg image,run through the YOLOv5 model and get annotations in a XML format.
 <details open>
<summary>Install</summary>
 
Clone repo and install [requirements.txt](https://github.com/aku134/Internship_task/blob/master/Part1/requirements.txt)
  
```bash
git clone https://github.com/aku134/Internship_task.git  # clone
cd Part1
pip install -r requirements.txt  # install
```
</details>
<details open>
<summary>Run</summary>
Run the following command to get annotations of the image in a XML file.
  
```bash
python detect.py --source data/images/bus.jpg
```
 </details>
 <details open>
<summary>Output</summary>

<img src="Readme_imgs/bus.jpg" height=400 width=350>
<img src="Readme_imgs/xml_file_ss.jpg" height=400 width=350>

</details>
The XML file is saved as result_to_xml.xml in the same directory.The image result is saved under runs/detect.

## Part2
### Objective
Given n number of unordered points,create a function that returns a polygon passing through all the points.
## Algorithm
<ul>
<li>The idea behind the solution is to find the leftmost and the rightmost points.We can do this by selecting the point with the least x coordinate and maximum x coordinate values respectively.</li>
<li>The next step is to consider an imaginary line passing through both these points.
All the points that lie above the line are stored in one array, A and the points below it are stored in another,B.</li>
<li>We can determine this by computing cross product of each point with the leftmost and the rightmost points.
If the value is positive i.e the point is in clockwise direction w.r.t leftmost point, the point lies above the line segment, if negative then below it.<br>
There could be a case where the value is 0 i.e the point is collinear with the leftmost and rightmost points.In that case we store the point in a third array, C.</li>
<li>Array A is then sorted in increasing order of their value (ascending) w.r.t to the x coordinate.
 Array B is sorted in decreasing order of their value (descending) w.r.t to the x coordinate.</li>
<li>The idea is to connect the points in clockwise direction while forming a polygon<br>
Finally leftmost point is added first to the final list followed by points in sorted array(ascending) A,rightmost point followed by points in sorted array(descending) B.If there is a collinear point, stored in array C that is added at last.</li><br>
 </ul>


<details open>
<summary>Install</summary>
Install tkinter which is an open source python package that helps create GUIs.

```bash
pip install tk
```
</details>
<details open>
<summary>Run</summary>

```bash
python app.py
```
</details>

### Example

<details open>
<summary>Input</summary>
Unordered points<br>
(300, 200): A, (500, 300): B, (200, 200): C, (300, 100): D, (400, 100): E, (300, 500): F

</details>
<details open>
<summary>Output</summary>
Ordered points:<br>
(200, 200): C,
(300, 500): F,
(500, 300): B,
(400, 100): E,
(300, 200): A,
(300, 100): D,<br><br>
<img src="Readme_imgs/polygon.jpg" width=500 height=450>

</details>
The polygon shape is drawn on tkinter canvas window.



