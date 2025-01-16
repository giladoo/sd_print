# Odoo PDF Report Redirect Module

## Overview
The Odoo PDF Report Redirect Module is designed to enhance the user experience by automatically redirecting PDF report downloads to a new tab. This allows users to easily view, print, and manage their reports directly from their browser, without the need for additional steps.

## Features
- **Automatic Redirect:** When generating a PDF report, users are automatically redirected to a new tab where the report opens.
- **Improved Usability:** Enhances the user experience by streamlining the process of viewing and printing reports.
- **Seamless Integration:** Easily integrates with existing Odoo report generation workflows.

## Installation
1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/giladoo/sd_print.git
    ```
2. Add the module to your Odoo `addons` directory.
3. Update the module list and install the "PDF Report Redirect" module from the Odoo app list.

## Usage
1. Navigate to the desired report in Odoo.
2. Click on the "Generate PDF" button.
3. The PDF report will automatically open in a new tab.

## Dependencies
- Odoo 15.0 or later

## Changes
- There is a function named `makeActionManager` which is in action_service.js file in web module.
    As it is not exported in odoo 15, I could not patch it directly. So I copy all the file and then I did some makeups to the links. 
    Then the `_triggerDownload` function inside of it changed to redirect to the file creation link instead of file download.

## Acknowledgements
- Special thanks to the Odoo community for their continuous support and inspiration.

## Contact
If you have any questions or feedback, please feel free to reach out to us at [homayounfar@msn.com].

