# Patchr
## Services

- Fix buggy apps based on repair specification (command line tool)
  - **Description:** Given a detailed repair specification, we patch the buggy app. 
  - **Input:** Each JSON file contains the following information corresponding to a bug at a location in the repository.
    - The bug type, repository it belongs to, file that contains the bug, class of the bug, method that contains the bug and the line number in the source code that contains the bug.

      Below is the snapshot of the JSON files. Filenames are of the format "bugName_lineNumber".json

      File: setTag_214.json

      ```json

      {
			"bugs": [
			{
				"bug": "view.setTag",
				"repo": "ianhanniballake/ContractionTimer",
				"file": "com.ianhanniballake.contractiontimer.ui.ViewFragment",
				"method": "onCreateView",
				"line": 214
			}
			]
      }
      ```

      File: getTag_120.json

      ```json

      {
			"bugs": [
			{
				"bug": "view.getTag",
				"repo": "ianhanniballake/ContractionTimer",
				"file": "com.ianhanniballake.contractiontimer.ui.ViewFragment",
				"method": "bindView",
				"line": 120
			}
			]

      }

      ``` 
  
      File: scanFile_29.json

      ```json

	{
			"bugs": [
			{
				"bug": "media.MediaScannerConnection",
  				"repo": "MediaScannerConnectionApp",
  				"file": "edu.colorado.cuplv.mediascannerconnectionapp.MediaScanner",
  				"class": "android.media.MediaScannerConnection",
  				"method": "onCreate",
  				"line": 29
			}
			]
	}
      ```

    - A query language that represents the repair specification for the bug. 
      
      - This is an ANTLR4 grammar representation of the repair specification which contains the method name and the arguments of the fixed API call, Android Code snippet specified as an Abstract Syntax Tree using ANTLR, parameters of the buggy API call and the rules which constitute the repair specification i.e., substitutions, insertions etc.
  
  - **Output:** File(s) containing the fix that complies to the repair specification are generated.

## Dependencies

- APIs
  - Recoder, version 0.97
- Built-time
  - sbt, version 0.13.7
  - Scala, version 2.11.7
  - ANTLR, version 4.5.1
- Runtime
  - Java, version 7,8

## Testing

- Example of an Input file would be the one of the JSON formats as mentioned above.

- The output file would be the transformed source code with the fix based on the repair specification.

  - The example below is the setTag bug which has been fixed. Output files shown below are prior and post applying the fix.

    Prior to the fix:

    ```java
    ...
    view.setTag(R.id.start_time, view.findViewById(R.id.start_time));
    ...
    ```

    Post applying the fix:

    ```java
    ...
    SparseArray sparseArray = new SparseArray();
    sparseArray.append(R.id.start_time, view.findViewById(R.id.start_time));
    SynthesizeTagWrapper synthesizeTagWrapper = new SynthesizeTagWrapper(sparseArray);
    view.setTag(R.id.start_time, synthesizeTagWrapper);
    ...
    ```

## Deployment Scripts

- **Repo Download and Dependencies:** Thanks to sbt, the dependency management is taken care and all the dependency information is present in the build.sbt file. A Travis-CI script file is written to download the repo from the Github repository. The script is located in the ```scripts``` folder.

- **Build the tool:**

- **Run the tool:**     
