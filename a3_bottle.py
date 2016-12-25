from bottle import route, run, debug, static_file, request

debug(True)


def htmlify(content, style, title):
    page = """
      <!DOCTYPE html>
      <html>
        <head>
          <title> 
          """ + title + """</title>
          <meta charset="utf-8" />
          <style>
        	.pagelocation {
			margin: 0px 450px;
          	}
    """ + style + """
    	  </style>
        </head>
        <body>
        <div class="pagelocation">
    """ + content + """
        </div>
        </body>
      </html>
    """
    return page


def main_page():
    html = """
			<h1>The name of the webpage</h1>
			<p>Please choose a type you would like to read about:</p>
		
			<form id="someid">
			<div>
				<select id="typefield" name="typefield" onchange="location = this.options[this.selectedIndex].value;" method="post">
					<option selected disabled>Options</option>
					<option value="/movies">Movies</option>
					<option value="/technology">Technology</option>
				</select>
			</div>
			</form>
			"""
    style = ""
    title = "MainPage"
    return htmlify(html, style, title)


def movies():
    html = """
		<h1>The name of the webpage</h1>
		<a href="/news_batman">
		<div class="img1">
		    <img src="https://www.comicbookmovie.com/images/articles/147511.jpg" alt="Batman">
		</div>
		    <h4 style="text-decoration: none">Ben Affleck Now Indicates That He'll Be Ready To Shoot His Solo BATMAN Movie In The Spring</h2>
		    <h5 style="text-decoration: none">Our last update on the progress of The Batman didn't seem particularly positive, but it now director Ben Affleck appears
		    to have committed to shooting the movie early next year. More past the jump...</h5>
		    <h5>Posted by: Mark Cassidy</h5>
		</a>
		<hr>
		"""
    style = """
		.img1 {
				float: left;
				margin-right: 20px;
				}
		h4 {
				text-decoration: none;
				color: black;
			}
		h5 {
				color: gray;
			}
		a {
		        text-decoration: none;
		    }
			"""
    title = "Movies"
    return htmlify(html, style, title)


def technology():
    html = """
		<h1>The name of the webpage</h1>
		<div class="img1">
		<img src="../batman.jpg" alt="Batman" width="250px">
		</div>
		<div class="mar">
		<h4><a href="/news_batman">THE BATMAN Expected To Begin Filming Spring 2017, According to AFFLECK</a></h2>
		<h6>Articles | Movies</h6>
		<hr>
		<p></p>
		</div>
		"""
    style = """
		.img1 {
				float: left;
				}
		h4 a {
				text-decoration: none;
				margin-left: 20px;
				color: black;
			}
		h6 {
				color: gray;
				text-indent: 20px;
			}
			"""
    title = "Technology"
    return htmlify(html, style, title)


comments = [
    {'name': 'Bruce Wayne',
     'gender': 'Male',
     'age': 35,
     'comment': 'It will be an awesome movie. You can be sure guys because I am Batman.'},
    {'name': 'Clark Kent',
     'gender': 'Male',
     'age': 36,
     'comment': 'I am proud of you bro. I am looking forward to see it.'}
]
value = 4.30


def news_batman():
    html = '''
				<h2>Ben Affleck Now Indicates That He'll Be Ready To Shoot His Solo BATMAN Movie In The Spring</h2>
				<img src="https://www.comicbookmovie.com/images/articles/banners/147511.jpg" alt="Ben Affleck">
				<p>Our last report on the status of the standalone <strong>Batman</strong> movie made it seem like the project was still quite a while away from shooting, with director 
				<strong>Ben Affleck</strong> appearing to suggest that the script wasn't even close to being completed.</p>
				Well, it seems the Live by Night star has now changed his tune in that regard.</p>
				<p>Variety caught up with Affleck at a tastemakers screening at New York’s Metrograph Theater last night, and he apparently indicated to them that 
				The Batman (if that is the title they go with) should be ready for a spring shoot. <strong>“We’re on the right track with that and everything is coming 
				together,”</strong> Affleck said. <strong>“We’re still finishing up a script. I’m very excited.”</strong></p>
				<p>While that definitely sounds more positive, there's still no official word on when cameras are expected to roll on <strong>The Batman</strong>, so until we 
				get that this should be taken as yet another conflicting report.</p>
				<p>What do you guys make of Affleck's apparent backtrack here?</p>
				
				<form action="/rate_submit" method="POST" id="rate" class="rateForm">

    				<fieldset>
        				<legend>Rating</legend>
        						<p>Please rate the post:</>
       							<p>
           						<input type="number" name="quantity" min="1" max="5">
           						<input type="submit" value="Rate" />
         						<label style="float: right">Total: <input type="text" class="num" name="total" readonly="readonly" value="''' + str(value) + '''"/></label>
        						</p>
        			</fieldset>
    			</form>
    			<br>
    			<fieldset>
    			<legend>Comments</legend>
    				<table>
    					<tr>
    						<th style="float:left">Name</th>
    						<th>Gender</th>
    						<th>Age</th>
    						<th></th>
    					</tr>'''
    for person in comments:
        html += '  <tr>\n'
        html += '    <td><strong>' + str(person['name']) + '</strong></td>\n'
        html += '    <td>' + str(person['gender']) + '</td>\n'
        html += '    <td>' + str(person['age']) + '</td>\n'
        html += '  </tr>\n'
        html += '  <tr>\n'
        html += '    <td>' + str(person['comment']) + '</td>\n'
        html += '  </tr>\n'
    html += '<tr>\n'
    html += '</table><br><br>\n'
    html += '<form method="POST" action="/add_submit">\n'
    html += '<fieldset>\n'
    html += '<legend>Add a new comment!</legend>\n'
    html += '  Name: <input type="text" name="name" /><br />\n'
    html += '''
		<form action="/add_submit">
  			<input type="radio" name="gender" value="Male" checked> Male<br>
  			<input type="radio" name="gender" value="Female"> Female<br>
  			<input type="radio" name="gender" value="Other"> Other<br> 
		</form> 
	'''
    html += '  Age: <input type="number" name="age" /><br /><br />\n'
    html += '  <textarea rows="5" cols="127" name="comment">'
    html += 'Enter your comment here!</textarea>'
    html += '  <input type="submit" value="Send the comment!"" />\n'
    html += '  </fieldset>\n'
    html += '</form>\n'
    html += '</fieldset>'
    style = """
			"""
    title = "Ben Affleck Now Indicates That He'll Be Raedy To Shoot His Solo BATMAN Movie In The Spring"
    return htmlify(html, style, title)


ini = 7
tot = 8


def rate_submit():
    title = "Your Rating"

    post_request = request.POST
    rate = int(post_request['quantity'])
    global value, ini, tot
    value = float(((ini * float(value)) + int(rate)) / tot)
    value = format(value, '.2f')
    ini += 1
    tot += 1

    html = "<p>Your rating for the post is " + str(rate) + """.</p>
			<form action="/news_batman">
   				<input type="submit" value="Turn back to the post!">
    		</form>
    		"""
    style = ""
    return htmlify(html, style, title)


def add_submit():
    post_request = request.POST

    name = str(post_request['name'])
    gender = str(post_request['gender'])
    age = int(post_request['age'])
    comment = str(request.forms.get('comment'))

    global comments
    comments += [{'name': name, 'gender': gender, 'age': age, 'comment': comment}]

    html = '''<p>You can see your comment below</p>
			<table>\n
			<tr>\n
                <th>Name</th>\n
                <th>Gender</th>\n
				<th>Age</th>\n
                <th></th>\n
            </tr>\n
            <tr>\n
 			<td><strong>''' + str(name) + '''</strong></td>\n    
 			<td>''' + str(gender) + '</td>\n' + '<td>' + str(age) + '''</td>\n
            </tr>\n
            <tr>\n
   			<td>''' + str(comment) + '</td>\n  </tr>\n </table>' + """
            <form action="/news_batman">
                <input type="submit" value="Turn back to the comments!">
            </form>
            """

    style = ""
    title = "Comments - Ben Affleck Now Indicates That He'll Be Raedy To Shoot His Solo BATMAN Movie In The Spring"
    return htmlify(html, style, title)


route('/mainpage', 'GET', main_page)
route('/movies', 'GET', movies)
route('/technology', 'GET', technology)
route('/news_batman', 'GET', news_batman)
route('/add_submit', 'POST', add_submit)
route('/rate_submit', 'POST', rate_submit)
run()
