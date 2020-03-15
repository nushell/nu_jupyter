from ipykernel.kernelbase import Kernel
import subprocess
import json

class NushellKernel(Kernel):
    implementation = 'Nushell'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {
        'name': 'Any text',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }
    banner = "Nushell kernel - let's have fun"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            command = 'nu -c "' + code.replace('"', '\\"') + ' | to-html"'

            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p_status = p.wait()


            if err:
                display_data = {
                    'data': {
                        "text/plain": err,
                    },
                    'metadata': {},
                }
                self.send_response(self.iopub_socket, 'display_data', display_data)
            else:
                display_data = {
                    'data': {
                        "text/html": output,
                    },
                    'metadata': {},
                }
                self.send_response(self.iopub_socket, 'display_data', display_data)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=NushellKernel)
