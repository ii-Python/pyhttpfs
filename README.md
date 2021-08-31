# pyhttpfs
---

Have you ever wanted a method of exploring a filesystem from a browser?
Perhaps for a quick development server, or for something more advanced such as a download server.

PyHTTPFS is designed to be just that, a filesystem explorer for HTTP.

---
PyHTTPFS is heavily based on the JS module `http-server`, [available here](https://www.npmjs.com/package/http-server). It is meant to be very lightweight and efficient, while also being robust and configurable.

---

#### Getting started
In order to get started, first clone the repository, ensure you have Python 3.7+, and then follow these instructions: 
- Install the requirements from `reqs.txt` (`pip install -r reqs.txt`)
- Ensure you have python scripts on your PATH

To begin hosting the server, you can simply run `pyhttpfs` from your terminal.
To customize the shared location, pass the `-l` location and specify a new one. For example, `pyhttpfs -l /home` would share the `/home` folder.

It is also worth noting that by default, **PyHTTPFS runs on port 8080**.


#### Configuration
In order to fully use PyHTTPFS to it's maximum potential, you'll have to configure it. The following options are available to you:
- `-b`, to bind to a specific address (eg. `-b 127.0.0.1`)
- `-p`, to bind to a specific port (eg. `-p 80`)
- `-l`, to share a specific location (eg. `-l /home`)