# Galaxy position finder 🌌

This project retrieves the **Right Ascension (RA)** and **Declination (Dec)** from the NASA/IPAC Extragalactic Database ([NED](https://ned.ipac.caltech.edu/)) of a list of galaxies and saves the results to a text file.



## 📜 **How It Works**
1. Reads galaxy names from `galaxies.txt`.  
2. Sends a **POST request** to the **NASA/IPAC Extragalactic Database (NED)** using `requests`.  
3. Extracts **Right Ascension (RA) and Declination (DEC)** from the JSON response.  
4. Saves the results in `galaxies_coords.txt`, ensuring the header is only added once.  



## 📌 **Output Format**
The results are stored in a tab-separated `.txt` file, for example:  
```
Galaxy Name	RA	DEC
NGC 4030	180.0984929	-1.1000504
NGC 4697	192.1495343	-5.8006418
NGC 4775	193.4404369	-6.622408

```
