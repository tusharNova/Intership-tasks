# WhatsApp to Google Drive Workflow

This n8n workflow allows users to interact with Google Drive through WhatsApp messages. It processes incoming WhatsApp messages, interprets commands, and performs corresponding actions on Google Drive.

## Features

- Process WhatsApp messages as commands for Google Drive operations
- Supported commands:
  - `list [folder]` - List files in specified folder (default: root)
  - `delete [filename]` - Delete specified file
  - `move [filename] to [folder]` - Move file to different folder
  - `summarize [filename]` - (Placeholder for future functionality)
- Send confirmation messages back via WhatsApp

## Workflow Components

1. **Webhook**: Receives incoming WhatsApp messages
2. **Code Node**: Parses the message and identifies the command
3. **Switch Node**: Routes to appropriate operation based on command
4. **Google Drive Nodes**: Perform the requested file operations
5. **Twilio Node**: Sends confirmation messages back to user

## Setup Instructions

### Prerequisites

1. n8n instance
2. Twilio account with WhatsApp enabled
3. Google Drive API access

### Configuration

1. **Twilio Credentials**:
   - Add your Twilio account credentials to the "Send an SMS/MMS/WhatsApp message" node

2. **Google Drive Credentials**:
   - Add your Google Drive OAuth2 credentials to all Google Drive nodes

3. **Webhook Configuration**:
   - Set up your Twilio WhatsApp webhook to point to this workflow's webhook URL

## Usage

Send WhatsApp messages in the following formats:

- To list files: `list [folder_name]` (folder_name is optional)
- To delete a file: `delete filename.txt`
- To move a file: `move filename.txt to folder_name`
- To summarize a file: `summarize filename.txt` (placeholder)

## Notes

- The workflow currently has placeholder functionality for the "summarize" command
- File operations are performed on the first matching file found
- Error handling can be enhanced based on specific requirements