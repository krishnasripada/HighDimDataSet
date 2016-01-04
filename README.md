# Patchr
## Services

- Fix buggy apps based on repair specification (command line tool)
  - **Description:** Given a detailed repair specification, we patch the buggy app. 
  - **Input:** Each JSON file contains information corresponding to a particular bug type.
    - The bug type, repository it belongs to, file that contains the bug, class of the bug, method that contains the bug and the line number in the source code that contains the bug.

      Below is the snapshot of the JSON files. Filenames are of the format "bugName".json

      File: setTag.json

      ```json

      {
			"bugs": [
			{
				"bug": "view.setTag",
				"repo": "ianhanniballake/ContractionTimer",
				"file": "com.ianhanniballake.contractiontimer.ui.ViewFragment",
				"method": "onCreateView",
				"line": 214
			},
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
  
      File: scanFile.json

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
  - Scala, version 2.11.7
  - ANTLR, version 4.5.1
- Runtime
  - Java, version 7,8
  - Android, version 5.0 and above  
