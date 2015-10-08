---
layout: defaultPlain
title: Weekly Bulletin
logoLink: /
menu1: Main Site
menu1Link: /
menu2: Current Students
menu2: /private/
---

<div class="container">
    <div class="row">
    {% for post in site.categories.bulletin %}
        <div class="col-md-4 col-sm-6 services-item">
            <div class="services-caption">
                <h4><a href="{{site.url}}{{site.baseurl}}{{ post.url }}">{{ post.title }}</a></h4>
            </div>
        </div>
    {% endfor %}
    </div>
</div>
