# Patchr
## Services

- Fix buggy apps based on repair specification (command line tool)
  - Description: Given a detailed repair specification, we patch the buggy app. 
  - Input: Each JSON file contains information corresponding to a particular bug. So fixing more than 1 bug type would require more than 1 JSON file to be provide which contains the following information.
    - The bug type, repository it belongs to, file that contains the bug, class of the bug, method that contains the bug and the line number in the source code that contains the bug.

      Format: setTag.json

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
  
      Format: scanFile.json

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
