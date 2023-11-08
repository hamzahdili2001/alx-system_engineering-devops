# Command line for the win:
This is command line challenge that I did as a challenge and an opportunity to
learn new things.

## about the challenge:
CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

## How I transfer the files to the sandbox:

1. Access Terminal: I opened my Terminal on my Windows I am using `WSL` so I
	 entered the folder with the `.png` files that I copied from my Windows to the
	Linux Folder.
2. Navigate to the Directory: I Navigate to that directory that I copied from my
	 Windows.
3. Install `SFTP` Client: I don't have it on my `WSL` so I installed it using:
	`sudo apt-get install openssh-client`
4. Use `SFTP` to transfer the files:
  `sftp user@example.com`
5. Uploaded the files: `put *.png` into the home directory and done.
