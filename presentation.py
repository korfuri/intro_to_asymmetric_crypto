import showtmux


class Presentation(showtmux.WithMdp, showtmux.Presentation):
    def present(self):
        self.wait("Live-demo of trusted CAs")
        self.new_window("demo")
        self.select_window("demo")

        self.wait("Let's look at the certificate authorities I trust")
        self.raw("awk -v cmd='openssl x509 -noout -subject' '/BEGIN/{close(cmd)};{print | cmd}' < /etc/ssl/certs/ca-certificates.crt | less")
        self.wait("run it")
        self.cmd(" ")
        self.wait("Enter tmux and explore the list - Staat der Nederlands is in there for a good example")
        self.wait("Remember to close less (q)")

        self.wait("Let's look at how I trust codam.com")
        self.raw("openssl s_client codam.com:443 | less")
        self.wait("run it")
        self.cmd(" ")
        self.wait("Enter tmux and scroll back up to take a look")

        self.wait("Back to slides")
        self.select_window(0)

    def slides_file(self):
        return 'intro_to_crypto.md'



p = Presentation("showtmux")
p.run()
