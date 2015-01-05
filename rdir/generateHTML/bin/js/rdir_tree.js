/**
 * Created by lhfcws on 15-1-5.
 */

var toggleDoc = function (this_dom) {
    _this = $(this_dom);

    var get_node_doc = function () {
        return _this.parent().parent().siblings(".node_doc");
    };

    var node_doc = get_node_doc();

    node_doc.toggle();
};


$(function () {
    var toggleChildren = function (_this, flag) {
//            _this = $(this);
        var myleft = parseInt(_this.css("margin-left"));
        var begin = false;
        var end = false;

        var getNodeFullname = function (t) {
            return t.children("div div.node_info").children("div div").children("span.node_fullname");
        };

        $("div.tree_node").each(function (index) {
            if (end) return;

            var t = $(this);
            if (begin && (myleft >= parseInt(t.css("margin-left"))))
                end = true;
            if (getNodeFullname(t).html().trim() == getNodeFullname(_this).html().trim()) {
                begin = true;
                return;
            }

            if (begin && !end) {
                if (flag)
                    t.show();
                else {
                    console.log(t.css("margin-left"));
                    t.hide();
                }
            }
        });
    };

    $("#header_doc_toggle").click(function () {
        $("#header_doc").toggle();
    });

    $("#show_all_doc").click(function () {
        $(".node_doc").each(function () {
            var _this = $(this);
            if (_this.parent().is(":visible"))
                _this.show();
        });
    });

    $("#hide_all_doc").click(function () {
        $(".node_doc").each(function () {
            $(this).hide();
        });
    });

    $(".fold_flag").click(function () {
        var _this = $(this);
        var fold_flag = _this.html();
        var tree_node = _this.parent().parent().parent();

        if (fold_flag == "-") {
            toggleChildren(tree_node, false);
            _this.html("+");
        }
        else if (fold_flag == "+") {
            toggleChildren(tree_node, true);
            _this.html("-");
        }
    });
});