
def js(url):
	pre = '''
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://code.jquery.com/ui/1.13.1/jquery-ui.min.js"></script>
<link rel="stylesheet" href="https://code.jquery.com/ui/1.13.1/themes/base/jquery-ui.css">

		<script>
    			$(function () {
        		$.ajax({
            		url: "'''
	post  = '''",
            dataType: "json",
            success: function (data) {
                $(".autocomplete").autocomplete({
                    source: function (request, response) {
                        var matcher = new RegExp("^" + $.ui.autocomplete.escapeRegex(request.term), "i");
                        response($.grep(data, function (item) {
                            return matcher.test(item);
                        }));
                    },
                    minLength: 1
                });
            }
        });
    });
</script>
'''
	return pre + url + post
