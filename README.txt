## Redacto README
----

**EXPERIMENTAL APPLICATION PROVIDED WITH NO GUARANTEES OR LIABILITY - Licensed under the GPL Tom Brown 2020**

## Dependencies
1. poppler-0.68.0

## Usage
1. In the config.ini specify the pdf input and output directories, this should be an absolute path e.g. C:\Users\tomsh\PycharmProjects\Redacto\pdf_input
2. The SplitIntoMultiplePages option can be True or False, if True the application will output separate PDFs for each page, otherwise you will get a single PDF
3. Run the exe, the application will poll the input directory every 10 seconds for new files processed PDFs will appear in the output directory
4. In the event of an application crash, clear out both the input and output directories of any files and restart the application

## Acknowledgements
* Icon by Freepik https://www.flaticon.com/free-icon/padlock_444378

## License
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.