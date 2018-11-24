
class HtmlOutputer():
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # 打开文件写模板， 也可以带入目录下写好的模板
        with open('output.html', 'w', encoding='utf-8') as fout:

            fout.write('<html>')
            fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
            fout.write('<link href="layout.css">')
            fout.write('<body>')
            fout.write('<table>')

            # ascii
            for data in self.datas:
                fout.write('<tr>')
                fout.write('<td>%s</td>' % data['url'])
                fout.write('<td>%s</td>' % data['title'])
                fout.write('<td>%s</td>' % data['summary'])
                fout.write('</tr>')



            fout.write('</table>')
            fout.write('</body>')
            fout.write('</html>')

            fout.close()
