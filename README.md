
<h1> facex-sample-codes </h1>
FaceX provides a face detection and face recognition web service that can be integrated to your apps with just a few lines of code.
It can scan uploaded image files or image URLs to perform. The complete documentation is provided in the <a href="https://documenter.getpostman.com/view/5211511/RWaDYCUN">link</a>.

The FaceX API is built on REST principles. Authenticated users can interact with any of our URIs by using
the specified HTTP request method.

<strong>The three APIs that we currently support are:</strong>
<ol type="1">
  <strong> <li> get_image_attr :</strong>  For detecting faces , gender detection , age range prediction and facial landmark. 
   </li>
   <li> <strong> compare_faces : </strong> For comaparing two faces to check if it belongs to the same person. </li>

   <strong> <li> get_face_vec :</strong> Get 128 dimensional feature vector describing a face for recognition and identification purpose. </li>
</ol>
The samplecodes in python ,php and jquery is provided in the repository files as below:
<ol type="1">
<strong><li> get_image_attr: </strong>
<ul>
<strong><li> python:</strong> pyhton -> facex_img.py  </li>
   <li> <strong> php:</strong> <ul> <strong><li> using file upload method:</strong> php -> facex_img_file.php </li>
           <li> <strong> using url method        : </strong> php -> facex_img-url.php  </li> </ul> </li>
  <li> <strong>  jquery:</strong> <ul> <strong> <li>  using file upload method: </strong> jquery -> facex_img_file.html </li>
                <li> <strong> using url method        : </strong> jquery -> facex_img-url.html </li> </ul>
 </ul>
</li>
<li>               
<strong>compare_faces:</strong>
<ul>
<li>
   <strong> python: </strong>pyhton -> facex_cmp.py</li>
 <li>  <strong> php:</strong> <ul> <li> <strong>sing file upload method: </strong> php -> facex_cmp_file.php </li>
          <li> <strong> using url method        : </strong> php -> facex_cmp-url.php </li> </ul> </li>
  <li> <strong> jquery: </strong> <ul> <li>  <strong> using file upload method:</strong> jquery -> facex_cmp_file.html</li>
  <li> <strong> using url method        : </strong>jquery -> facex_cmp-url.html</li> </ul> </li>
</ul>
</li>
<li>
<strong> get_face_vec: </strong>
<ul>
<li>
   <strong> python:</strong>  pyhton -> facex_vec.py</li>
  <li> <strong> php:</strong> <ul> <li> <strong> using file upload method:</strong> php -> facex_vect_file.php </li>
        <li>   <strong> using url method        : </strong> php -> facex_vec-url.php </li> </ul> </li>
  <li> <strong> jquery:</strong> <ul> <li>  <strong> using file upload method:</strong> jquery -> facex_vec_file.html </li>
             <li>  <strong> using url method        : </strong>jquery -> facex_vec_url.html </li> </ul> </li>
               
 </li>
           
 </ol>
         
        
