<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Numbers API</title>
    <!-- TODO: uncomment <meta name="viewport" content="width=device-width, initial-scale=1.0">-->
    <meta
      name="description"
      content="An API for interesting facts about numbers."
    />
    <meta name="author" content="David Hu, Mack Duan" />

    <!-- Le HTML5 shim, for IE6-8 support of HTML elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Le styles -->
    <link href="css/screen.css" rel="stylesheet" type="text/css" />

    <!-- Le fav and touch icons -->
    <link rel="shortcut icon" href="img/favicon.ico" />

    <!-- Le Google Analytics -->
    <script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(["_setAccount", "UA-29155677-1"]);
      _gaq.push(["_trackPageview"]);

      (function () {
        var ga = document.createElement("script");
        ga.type = "text/javascript";
        ga.async = true;
        ga.src =
          ("https:" == document.location.protocol
            ? "https://ssl"
            : "http://www") + ".google-analytics.com/ga.js";
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(ga, s);
      })();
    </script>
  </head>
  <body>
    <div id="body-inner">
      <div class="body-container">
        <div id="logo-outer">
          <h1 class="logo">Numbers<span id="second-word">API</span></h1>
        </div>

        <span id="tagline">
          An API for interesting facts about numbers
        </span>
        <ul id="tagline-alternates" style="display: none;">
          <li>Bring meaning to your metrics and stories to your dates</li>
          <li>An API for interesting facts about numbers</li>
          <li>Bring your metrics and dates to life</li>
          <li>Let your metrics tell tales with our API of number facts</li>
          <li>What tales do your metrics tell?</li>
          <li>Let your statistics tell tales and dates come to life</li>
        </ul>

        <section id="usage-outer">
          <div id="usage">
            <div id="examples">
              <div class="example">
                <h2>Math</h2>
                <div class="example-box">
                  <a href="#5/math">numbersapi.com/5/math</a>
                  <div class="api-result scroll">
                    5 is the number of platonic solids.
                  </div>
                </div>
              </div>
              <div class="example">
                <h2>Trivia</h2>
                <div class="example-box">
                  <a href="#42">numbersapi.com/42</a>
                  <div class="api-result scroll">
                    42 is the number of little squares forming the left side
                    trail of Microsoft's Windows 98 logo.
                  </div>
                </div>
              </div>
              <div class="example">
                <h2>Date</h2>
                <div class="example-box">
                  <a href="#1/29/date"
                    >numbersapi.com/1/29/date</a
                  >
                  <div class="api-result scroll">
                    January 29th is the day in 1886 that Karl Benz patents the first successful gasoline-driven automobile.
                  </div>
                </div>
                <!-- example-box -->
              </div>
              <!-- example -->
            </div>
            <!-- examples -->
          </div>
          <!-- usage -->
        </section>

        <section id="sandbox-outer">
          <div id="sandbox">
            <div class="arrow"></div>
            <div id="sandbox-text">Try it out!</div>
            <div id="outer-search">
              <div id="search">
                <div id="search-box">
                  <label><a id="search-link">numbersapi.com/</a></label>
                  <span><input id="search-text" type="text" /></span>
                </div>
                <!-- TODO: fix scroll for sandbox. shouldn't be too much of an issue yet, since facts generally should not be long enough to overflow the container -->
                <div id="search-result" class="api-result">
                  <div id="counter"></div>
                  <span id="result-temporary-text"
                    >Please enable JavaScript to use this API browser.</span
                  >
                  <div style="display: none;" id="add-fact-area">
                    <div id="add-fact-prefix">hello there</div>
                    <textarea id="add-fact-text" rows="3"></textarea>
                  </div>
                </div>
                <a id="add-fact-label" style="display: none;" href="#"
                  >+ Add a fact</a
                >
              </div>
              <div id="search-examples">
                <h3>Random</h3>
                <ul>
                  <li><a href="#random/trivia">random/trivia</a></li>
                  <li><a href="#random/year">random/year</a></li>
                  <li><a href="#random/date">random/date</a></li>
                  <li><a href="#random/math">random/math</a></li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        <section id="visitors">
          <div class="gradient-fill"></div>
          <div class="flare-background"></div>

          <div id="addthis">
            <div class="addthis_toolbox addthis_32x32_style">
              <a class="addthis_button_preferred_1"></a>
              <a class="addthis_button_preferred_2"></a>
              <a class="addthis_button_preferred_3"></a>
              <a class="addthis_button_preferred_4"></a>
              <a class="addthis_button_compact"></a>
              <a class="addthis_counter addthis_bubble_style"></a>
            </div>
          </div>

          <div
            class="visit-text"
            title="Generated using http://numbersapi.com/15?notfound=floor&fragment"
          >
            <a href="#15?notfound=floor&fragment"
              >This page has been shared more times than the number of days in each of the 24 cycles of the Chinese calendar.</a
            >
          </div>
          <div class="gradient-fill"></div>
        </section>

        <section id="api-outer">
          <div id="api">
            <h1>API Reference</h1>
            <p>Bring meaning to your metrics and stories to your dates with our API of interesting number facts.</p>
<h2 id="url-structure">URL Structure</h2>
<p>Just hit <code><a href="http://numbersapi.com/">http://numbersapi.com/</a><strong>number</strong>/<strong>type</strong></code> to get a plain text response, where</p>
<ul>
<li><strong><code>type</code></strong> is one of <code>trivia</code>, <code>math</code>, <code>date</code>, or <code>year</code>. Defaults to <code>trivia</code> if omitted.</li>
<li><strong><code>number</code></strong> is<ul>
<li>an integer, or</li>
<li>the keyword <code>random</code>, for which we will try to return a random available fact, or</li>
<li>a day of year in the form <code><strong>month</strong>/<strong>day</strong></code> (eg. <code>2/29</code>, <code>1/09</code>, <code>04/1</code>), if <strong><code>type</code></strong> is <code>date</code></li>
<li><a href="#batching">ranges of numbers</a></li>
</ul>
</li>
</ul>
<pre>
http://numbersapi.com/42
&rArr; 42 is the result given by Google and Bing for the query "the answer to life the universe and everything".

http://numbersapi.com/2/29/date
&rArr; February 29 is the day in 1504 that Christopher Columbus uses his knowledge of a lunar eclipse to convince Native Americans to provide him with supplies.

http://numbersapi.com/random/year
&rArr; 2013 is the year that China will attempt its first unmanned Moon landing.
</pre>

<h2 id="usage-examples">Usage Examples</h2>
<h3 id="jquery">jQuery</h3>
<p>HTML:</p>
<pre><code>We now have more users than &lt;span id=&quot;number&quot;&gt;&lt;/span&gt;!</code></pre>
<p>JavaScript:</p>
<pre><code>$.get(&#39;http://numbersapi.com/1337/trivia?notfound=floor&amp;fragment&#39;, function(data) {
    $(&#39;#number&#39;).text(data);
});</code></pre>
<p>Direct cross-origin requests like this are possible on browsers that support <a href="http://en.wikipedia.org/wiki/Cross-Origin_Resource_Sharing">CORS</a>. Live demo on <a href="http://jsfiddle.net/divad12/ffHEh/">JSFiddle</a>.</p>
<h3 id="jsonp">JSONP</h3>

<p>...is supported with the query field <a href="#callback"><code>callback</code></a>:</p>
<pre><code>&lt;span id=&quot;number-fact&quot;&gt;&lt;/span&gt;

&lt;script&gt;
    function showNumber(str) {
        document.getElementById(&#39;number-fact&#39;).innerText = str;
    }

    (function() {
        var scriptTag = document.createElement(&#39;script&#39;);
        scriptTag.async = true;
        scriptTag.src = &quot;http://numbersapi.com/42/math?callback=showNumber&quot;;
        document.body.appendChild(scriptTag);
    })();
&lt;/script&gt;</code></pre>
<p>Live demo on <a href="http://jsfiddle.net/divad12/4A6Pw/">JSFiddle</a>.</p>
<h3 id="single-script-tag">HTML Embed</h3>

<p>Add <code>write</code> to your query string to have the response text wrapped in <code>document.write()</code>. Now you can stick just a single <code>&lt;script&gt;</code> directly where the fact should go.</p>
<pre><code>Did you know 2012 is the year that &lt;script src=&quot;http://numbersapi.com/2012/year?write&amp;fragment&quot;&gt;&lt;/script&gt;?</code></pre>
<p>Note that this may <a href="http://developer.yahoo.com/performance/rules.html#js_bottom">degrade page load speed</a>. Live demo on <a href="http://jsfiddle.net/divad12/vd58j/">JSFiddle</a>.</p>
<h2 id="query-parameter-options">Query Parameter Options</h2>
<h3 id="fragment">Fragment</h3>
Return the fact as a sentence fragment that can be easily included as part of a larger sentence. This means that the first word is lowercase and ending punctuation is omitted. For trivia and math, a noun phrase is returned that can be used in a sentence like "We now have more users than [fact as fragment]!".

<pre>
http://numbersapi.com/23/trivia?fragment
&rArr; the number of times Julius Caesar was stabbed

http://numbersapi.com/1969/year?fragment
&rArr; an estimated 500 million people worldwide watch Neil Armstrong take his historic first steps on the Moon
</pre>

<h3 id="notfound">Notfound</h3>
<p>The <code>notfound</code> field tells us what to do if the number is not found. You can give us</p>
<ul>
<li><code>default</code> to return one of our pre-written missing messages, or a message you supply with the <a href="#default"><code>default</code></a> query field. This is the default behaviour.<pre>http://numbersapi.com/314159265358979
&rArr; 314159265358979 is a boring number.</pre></li>
<li><code>floor</code> to round down to the largest number that does have an associated fact, and return that fact.<pre>http://numbersapi.com/35353?notfound=floor
&rArr; 35000 is the number of genes in a human being.</pre></li>
<li><code>ceil</code>, which is like <code>floor</code> but rounds up to the smallest number that has an associated fact.<pre>http://numbersapi.com/-12344/year?notfound=ceil
&rArr; 98 BC is the year that the Senate passes the Lex Caecilia Didia which bans omnibus bills.</pre>

</li>
</ul>
<p>Combine with the <a href="#fragment">fragment</a> option to produce interesting facts about, for example, <a href="#visitors">the number of page shares</a>.</p>
<h3 id="default">Default</h3>
The value of the `default` query field tells us what to return if we don't have a fact for the requested number.

<pre>
http://numbersapi.com/1234567890987654321/year?default=Boring+number+is+boring.
&rArr; Boring number is boring.
</pre>

<h3 id="callback">Callback</h3>
To use [JSONP](http://en.wikipedia.org/wiki/JSONP), pass to the `callback` query the name of the JavaScript function to be invoked. The response will be that function called on the fact text as a string literal.

<pre>
http://numbersapi.com/42/math?callback=showNumber
&rArr; showNumber("42 is the 5th Catalan number.");
</pre>

<p>See the <a href="#jsonp">JSONP usage example</a>.</p>
<h3 id="write">Write</h3>
Returns the text response wrapped in a call to [`document.write()`](https://developer.mozilla.org/en/document.write). Note that using this query parameter is equivalent to and just a shorthand of `?callback=document.write`.

<pre>
http://numbersapi.com/42/math?write
&rArr; document.write("42 is the 5th Catalan number.");
</pre>

<p>See the <a href="#single-script-tag">HTML embed tag usage example</a>.</p>
<h3 id="min-and-max">Min and Max</h3>
<p>Restrict the range of values returned to the inclusive range [<strong><code>min</code></strong>, <strong><code>max</code></strong>] when <code>random</code> is given as the number.</p>
<pre>
http://numbersapi.com/random?min=10&max=20
13 is the number of provinces and territories in Canada.
</pre>

<h3 id="json">Json</h3>
Include the query parameter `json` or set the HTTP header `Content-Type` to `application/json` to return the fact and associated meta-data as a JSON object, with the properties:

<ul>
<li><code>text</code>: A string of the fact text itself.</li>
<li><code>found</code>: Boolean of whether there was a fact for the requested number.</li>
<li><code>number</code>: The floating-point number that the fact pertains to. This may be useful for, eg. a <code>/random</code> request or <code>notfound=floor</code>. For a date fact, this is the 1-indexed day of a leap year (eg. 61 would be March 1st).</li>
<li><code>type</code>: String of the category of the returned fact.</li>
<li><code>date</code> (sometimes): A day of year associated with some year facts, as a string.</li>
<li><code>year</code> (sometimes): A year associated with some date facts, as a string.</li>
</ul>
<pre>
http://numbersapi.com/random/year?json
&rArr; {
    "text": "2012 is the year that the century's second and last solar transit of Venus occurs on June 6.",
    "found": true,
    "number": 2012,
    "type": "year",
    "date": "June 6"
}
</pre>

<h2 id="batching">Batch Requests</h2>

<p>To get facts about multiple numbers in one request, specify ranges for <code><strong>number</strong></code> in <code><a href="http://numbersapi.com/">http://numbersapi.com/</a><strong>number</strong>/<strong>type</strong></code>.</p>
<p>A number range (inclusive) is specified as <code><strong>min</strong>..<strong>max</strong></code>. Separate multiple ranges and individual numbers with <code>,</code> (a comma).</p>
<p>The response format will always be a JSON map from numbers to facts, of at most 100 numbers. The query parameter <a href="/#json"><code>json</code></a> may still be used to specify whether individual facts will be returned as string literals or JSON objects.</p>
<pre>
http://numbersapi.com/1..3,10
&rArr; {
    "1": "1 is the number of dimensions of a line.",
    "2": "2 is the number of polynucleotide strands in a DNA double helix.",
    "3": "3 is the number of sets needed to be won to win the whole match in volleyball.",
    "10": "10 is the highest score possible in Olympics gymnastics competitions."
}
</pre>

          </div>
        </section>
      </div>
      <!-- /body-container -->

      <footer>
        <div>
          <p>
            Hacked up by
            <a href="http://david-hu.com/2012/03/05/announcing-numbers-api.html"
              >David</a
            >
            and <a href="http://mduan.com">Mack</a>. We want your feedback! Tell
            us what you use this for.
          </p>
          <p><a href="mailto:info@numbersapi.com">numbersapi@gmail.com</a></p>
        </div>
      </footer>

      <!-- Le javascript
    ================================================== -->
      <!-- Placed at the end of the document so the pages load faster -->
      <script
        src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"
        type="text/javascript"
      ></script>
      <script src="/js/jquery.mousewheel.js" type="text/javascript"></script>
      <script src="/js/jquery.counter.js" type="text/javascript"></script>
      <script src="/js/jquery.lionbars.0.3.js" type="text/javascript"></script>

      <noscript>
        <!-- TODO: figure out how to add styles via import stylesheet -->
        <style type="text/css"></style>
      </noscript>

      <!-- AddThis sharing icons -->
      <script>
        var addthis_config = {
          data_ga_tracker: "UA-29155677-1",
          data_ga_property: "UA-29155677-1",
          data_ga_social: true,
          services_exclude: "print",
          ui_cobrand: "Numbers API",
          ui_header_color: "#02273f",
          ui_header_background: "#cce4f4"
        };
        var addthis_share = {
          url: "http://numbersapi.com",
          description: "An API for interesting facts about numbers.",
          templates: {
            twitter:
              "An API for interesting facts about numbers: http://numbersapi.com"
          }
        };
      </script>
      <script
        type="text/javascript"
        src="http://s7.addthis.com/js/250/addthis_widget.js#pubid=ra-4f52dad55e864066"
      ></script>

      <script src="js/shared_utils.js"></script>
      <script src="js/script.js"></script>
    </div>
    <!-- #body-inner -->
    <!-- another comment -->
  </body>
</html>
