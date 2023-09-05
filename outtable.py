import docx


def out_table(output_file, output_content):
    doc = docx.Document(R"表格模板.docx")
    table = doc.tables[0]
    index = 0
    for each in output_content:
        index += 1
        table.add_row()
        table.rows[index].cells[0].text = str(index)
        table.rows[index].cells[1].text = str(each)
    doc.save(output_file)


if __name__ == '__main__':
    out_table(R"out.docx",
              [11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111, 222, 333, 444, 555])
