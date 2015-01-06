/**
 * Main logic of the tree page.
 * Created by lhfcws on 15-1-5.
 */

/**
 * Hide / show the doc of the node.
 * It will be invoked by onclick attr in the dom, so I put it in global space.
 * @param this_dom
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
    /**
     * Hide / show all the children of the node.
     * @param _this
     * @param flag
     */
    var toggleChildren = function (_this, flag) {
        var myleft = parseInt(_this.css("margin-left"));
        var begin = false;
        var end = false;

        var getNodeFullname = function (t) {
            return t.children("div div.node_info").children("div div").children("span.node_fullname");
        };

        /**
         * Iter all the .tree_node to find the children
         */
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
                    t.hide();
                }
            }
        });

        checkFlag();
    };

    /**
     * Recheck the fold flag
     */
    var checkFlag = function () {
        // true -> +, false -> -
        var size = $(".tree_node").length;
        var flags = Array(size);
        for (var i = 0; i < size; i++) flags[i] = false;

        $(".tree_node").each(function (index) {
            var _this = $(this);
            if (!_this.is(":visible")) {
                if (index > 0)
                    flags[index - 1] = true;
            }
        }).each(function (index) {
            if (flags[index])
                $(this).children("div div.node_info").children("div div").children("span.fold_flag").html("+");
            else
                $(this).children("div div.node_info").children("div div").children("span.fold_flag").html("-");
        });
    };

    /**
     * Show the nodes with suitable layer preference.
     */
    $("#choose_layer").change(function () {
        var layer = $("#choose_layer").val();
        if (layer < 0) return;
        var limit_left = layer * 50;

        $("div.tree_node").each(function (index) {
            var t = $(this);
            if ((limit_left >= parseInt(t.css("margin-left"))))
                t.show();
            else
                t.hide();
        });

        checkFlag();
    });

    /**
     * Hide / show the header_doc
     */
    $("#header_doc_toggle").click(function () {
        $("#header_doc").toggle();
    });

    /**
     * Show doc of all nodes.
     */
    $("#show_all_doc").click(function () {
        $(".node_doc").each(function () {
            var _this = $(this);
            if (_this.parent().is(":visible"))
                _this.show();
        });
    });

    /**
     * Hide doc of all nodes.
     */
    $("#hide_all_doc").click(function () {
        $(".node_doc").each(function () {
            $(this).hide();
        });
    });

    /**
     * The flag + / - just like that in the file explorer.
     */
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

        checkFlag();
    });
});
