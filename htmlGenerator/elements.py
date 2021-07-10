class htmlElemets:

    def __init__(self):
        self.body = '''<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>SKETCH TO HTML</title>
                            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
                                integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
                            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
                                integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
                                crossorigin="anonymous"></script>
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"
                                integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"
                                crossorigin="anonymous"></script>
                        </head>
                        <body">
                        <div class="container body-content" style="padding:30px">
                        <div class="container" style="padding-top:20px;position: relative;">\n'''

    def Button(self, corX, corY, width, height):

        button = '<div class="row justify-content-center text-center"  style="padding-top:20px;display: inline-block;position: absolute;top: '+str(corY)+'px;left:'+str(corX)+'px">'
        button += '<button class="btn btn-primary" type="button" style = "' 
        button += 'width: ' + str(width) 
        button += 'px; height: ' + str(height) + 'px;"' 
        button += '>Click Me!</button></div>'
        self.body += button
        self.body += '<br>\n'

    def Label(self, corX, corY):

        label = '<div class="row justify-content-center "   style="padding-top:20px;display: inline-block;position: absolute;top: '+str(corY)+'px;left:'+str(corX)+'px;">'
        label += '<label class="row justify-content-center "'
        label += '>Label</label></div>'
        self.body += label
        self.body += '<br>\n'

    def Image(self, corX, corY, width, height):

        image = '<div class="row justify-content-center text-center"   style="padding-top:20px;display: inline-block;position: absolute;top: '+str(corY)+'px;left:'+str(corX)+'px;">'
        image += '<img src="https://sketch2code.azurewebsites.net/Content/img/fake_img.svg" class="rounded"'
        image += ' alt="Image" width=' + str(width) 
        image += ' height=' + str(height) + '/></div>'
        self.body += image
        self.body += '<br>\n'

    def TextBox(self, corX, corY, width, height):

        textBox = '<div class="col">'
        textBox += '<input type="text" style = "position:absolute; left: ' + str(corX) 
        textBox += 'px; top: ' + str(corY) + 'px; width:' + str(width) 
        textBox += 'px; height: ' + str(height) + 'px;"' 
        textBox += ' id="lname" name="TextBox"></input></div>' 
        self.body += textBox
        self.body += '<br>\n'

    def CheckBox(self, corX, corY):

        checkBox = '<div class="form-check" style="display: inline-block;position: absolute;top: '+str(corY)+'px;left:'+str(corX)+'px;">'
        checkBox += '<input class="form-check-input" type="checkbox"'
        checkBox += 'id="lname" name="CheckBox"></input></div>' 
        self.body += checkBox
        self.body += '<br>\n'

    def RadioButton(self, corX, corY):

        radioButton = '<div class="form-check" style="display: inline-block;position: absolute;top: '+str(corY)+'px;left:'+str(corX)+'px;">'
        radioButton += '<input class="form-check-input" type="radio"' 
        radioButton += 'id="lname" name="RadioButton"></input></div>' 
        self.body += radioButton
        self.body += '<br>\n'

    def Table(self, rows, cols, corX, corY):
        
        table = '<div class="row justify-content-center text-center"  style="padding-top:10px;display: inline-block;position: absolute;top: '+str(corY)+'px;left:'+str(corX)+'px;">'
        table += '<table class="row justify-content-center text-center" border="1">'
        for row in range(rows):
            table += '<tr>'
            for col in range(cols):
                table += '<td> data (' + str(row) + ',' + str(col) + ') </td>'
            table += '</tr>'

        table += '</table></div>'            

        self.body += table
        self.body += '<br>\n'

    def Heading(self, corX, corY):
        self.body += '<div class="row justify-content-center text-center"  style="padding-top:10px;display: inline-block;position: absolute;top: '+str(corY)+'px;left:'+str(corX)+'px;">'
        self.body += '<h1>Heading</h1></div>'
        self.body += '<br>\n'

    def Link(self, corX, corY):
        link = '<div class="col">'
        link += '<a href = "#" style="position:absolute; left: ' + str(corX) 
        link += 'px; top: ' + str(corY) 
        link += 'px;" >Link</a></div>'
        self.body += link
        self.body += '<br>\n'

    def Select(self, corX, corY):
        
        self.body += '<div class="row justify-content-center text-center"  style="display: inline-block;position: absolute;top: '+str(corY)+'px;left:'+str(corX)+'px;">'
        self.body += '''<select name="cars" id="cars">
                <option value="volvo">Volvo</option>
                <option value="saab">Saab</option>
                <option value="mercedes">Mercedes</option>
                <option value="audi">Audi</option>
                </select></div>'''
        self.body += '<br>\n'

    def textArea(self, corX, corY, width, height):

        area = '<div class="row justify-content-center"   style="padding-top:20px;display: inline-block;position: absolute;top: '+str(corY)+'px;left:'+str(corX)+'px;">'
        area += '<textarea class="form-control" style="'
        area += 'width: ' + str(width) + 'px; height: ' + str(height)
        area += 'px;" id="w3review" name="w3review" rows="4" cols="50">' 
        area += 'TextArea</textarea></div>'
        self.body += area
        self.body += '<br>\n'

    def Pagination(self, corX, corY):

        self.body += '<div class="row justify-content-center text-center"  style="padding-top:30px;display: inline-block;position: absolute;top: '+str(corY)+'px;left:'+str(corX)+'px;">'
        self.body += '''
        <div class="pagination">
        <a href="#">&laquo;</a>
        <a href="#">1</a>
        <a class="active" href="#">2</a>
        <a href="#">3</a>
        <a href="#">4</a>
        <a href="#">5</a>
        <a href="#">6</a>
        <a href="#">&raquo;</a>
        </div></div>
        '''
        self.body += '<br>\n'

    def Paragraph(self, corX, corY):

        self.body += '<div class="row justify-content-center text-center"  style="padding-top:10px;display: inline-block;position: absolute;top: '+str(corY)+'px;left:'+str(corX)+'px;">'
        self.body += '<p>This is a paragraph.</p><br><p>This is another paragraph.</p></div>'
        self.body += '<br>\n'

    def Carousel(self, corX, corY, width, height):
        pass

    def isEnd(self):
        self.body += '</div></div></body></html>'
        return self.body