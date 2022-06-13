import pdfkit, os

config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}
# mdo = markdown.markdown('#' + data['title'] + '\n' + data['date'].split(' ')[0] + '  |  ' + data['tags'] + '\n\n' + data['text'], output_format='html5')



mdo = '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style type="text/css">
                body {
                    font-family: sans, Arial;
                }
                img {
                    width: 50%;
                    height: auto !important;
                    margin-right: 20px;
                    margin-top: 20px;
                    margin-bottom: 20px;
                    float: left;
                }
                hr, .userRThumb {
                    display: none;
                }
                .parent-shareBox, .tip-us-email-container {
                    display: none;
                }

            </style>
        </head>
        <body>
        <h1>Manchester Orders Its First Electric Buses</h1>2014-04-16  |  <br/><br/><ul style="list-style:none;"><li style="font-size:1.0em">england</li><li style="font-size:1.0em">greater manchester’s</li><li style="font-size:1.0em">london</li><li style="font-size:1.0em">manchester city</li></ul><br/><div class="postContent content-wrapper">   <div id="div-topcustombanner">  </div> <div class="postBody description e-content"> <section contenteditable="false" data-id="3935755" data-widget="image" draggable="true"><img alt="BYD ebus Enters Service in London" draggable="false" height="9" src="https://cdn.motor1.com/images/mgl/nEOpy/s3/manchester-orders-its-first-electric-buses.jpg" srcset="https://cdn.motor1.com/images/mgl/nEOpy/s3/manchester-orders-its-first-electric-buses.jpg 1x, https://cdn.motor1.com/images/mgl/nEOpy/s2/manchester-orders-its-first-electric-buses.jpg 2x" width="16"/> <p class="photo-title">BYD ebus Enters Service in London</p> </section> <p>Manchester joins several other cities in England with EV buses as Transport for Greater Manchester (TfGM) orders 13 Versa hybrid 12m-long school buses and 3 Versa 9.7m-long electric buses. Those three electric buses will be the very first in Manchester and should go into operation in a few months.</p> <p>Electric buses, bought thanks to support from the Department for Transport’s Green Bus Fund, will operate on the Metroshuttle routes linking the main rail stations, car parks, shopping areas and businesses in Manchester city center.</p><div class="m1_MobileMPU"></div> <p>Howard Hartley, TfGM Head of Bus, remarked:</p> <blockquote> <p><em>“We are committed to investing in buses with low carbon emissions and strong environmental credentials as part of a collective effort with operators to make Greater Manchester’s bus network – which caters for 216 million journeys a year – as green as possible.”</em></p> <p><em>“We have been happy with the performance and reliability of our current buses, and the support we have received from Optare, so are pleased to be expanding the number of hybrid vehicles within our fleet.”</em></p> </blockquote> <p>John Horn, Sales Director at Optare, commented:</p> <blockquote> <p><em>“Optare has had a strong start to 2014, so we are particularly pleased to announce another high value order. Transport for Greater Manchester’s decision to invest in more of Optare’s advanced hybrid and electric powered buses is a great testament to the reliability and cost effectiveness of our vehicles.”</em></p> </blockquote> </div> <!-- new gallery place, attached gallery --> <!-- Author info bottom --> <div class="postAuthorBox withAvatar" xmlns="http://www.w3.org/1999/xhtml"> <div class="postAuthorThumb"> <a class="userRThumb" href="/info/team/mark-kane/"> <picture class="lazyload"> <source data-srcset="https://cdn.motor1.com/images/atr/vmq/s3/mark-kane1.webp" type="image/webp"/> <source data-srcset="https://cdn.motor1.com/images/atr/vmq/s3/mark-kane1.jpg" type="image/jpeg"/> <img alt="Mark Kane" height="1" loading="lazy" src="https://cdn-3.motorsport.com/static/images/sizers/1x1_2.gif" width="1"> </img></picture> </a> </div> <div class="postAuthorInfo"> <div class="postAuthor"> <span class="name"> <span class="label">By</span>: <a class="author" content="Mark Kane" href="/info/team/mark-kane/">Mark Kane</a> </span> </div> </div> <div class="big-shareBox shareBox share-box-dropdown to-down" slot="share-box"><div class="share-box-wrapper"><span class="shareBox-separator" data-button="" data-id="toggleBox" data-static="" data-value="share-list-1653872285" onclick=""> <span class="active"><span class="icon-plus">+</span></span><span class="passive"><span class="icon-plus">+</span></span></span><a aria-label="share" class="share-button share-button-gallery" href="https://insideevs.com/news/321786/manchester-orders-its-first-electric-buses/" rel="nofollow noopener"><span class="icon share-empty"></span></a></div></div> </div> <div class="clear"></div> <div class="parent-shareBox parent-shareBox-bottom"> <div id="div-bottomcustombanner">  </div> <div class="big-shareBox shareBox share-box-dropdown to-down" slot="share-box"><div class="share-box-wrapper"><span class="shareBox-separator" data-button="" data-id="toggleBox" data-static="" data-value="share-list-1653871990" onclick=""> <span class="active"><span class="icon-plus">+</span></span><span class="passive"><span class="icon-plus">+</span></span></span><a aria-label="share" class="share-button share-button-gallery" href="https://insideevs.com/news/321786/manchester-orders-its-first-electric-buses/" rel="nofollow noopener"><span class="icon share-empty"></span></a></div></div> </div> <div class="tip-us-email-container"> <div class="tip-us-email"> <span>Got a tip for us? Email:</span> <a href="mailto: tips@insideevs.com?subject=manchester-orders-its-first-electric-buses"> tips@insideevs.com </a> </div> </div> <!-- new outbrain setup --> <div id="outbrain-wrapper-first"> <div class="outbrain_service" style="min-height: 1px;"> </div> </div> </div>
        </body>
        <html>
    '''

pdfkit.from_string(mdo, output_path=os.path.join(os.getcwd(), 'test_aus' + '.pdf'),
                   options=options, configuration=config)

