import re
from dash import hooks
from typing import Union


def setup_performance_monitor_plugin(
    script_src: str = "https://cdn.jsdelivr.net/npm/stats.js@latest/build/stats.min.js",
    left: Union[int, float] = 0,
    top: Union[int, float] = 0,
    opacity: Union[int, float] = 0.9,
    zIndex: int = 10000,
):
    """Setup the performance monitor plugin

    Args:
        script_src (str, optional): The source link of the origin stats.js script, other commonly used options include public CDN sources such as https://unpkg.com/stats.js@latest/build/stats.min.js and https://registry.npmmirror.com/stats.js/latest/files/build/stats.min.js. Defaults to "https://cdn.jsdelivr.net/npm/stats.js@latest/build/stats.min.js".
        left (Union[int, float], optional): The left pixel position of the monitor. Defaults to 0.
        top (Union[int, float], optional): The top pixel position of the monitor. Defaults to 0.
        opacity (Union[int, float], optional): The opacity of the monitor. Defaults to 0.9.
        zIndex (int, optional): The z-index of the monitor. Defaults to 10000.
    """

    @hooks.index()
    def add_stats_js(app_index: str):
        # Extract the last line of the footer part
        match = re.findall("[ ]+</footer>", app_index)

        if match:
            # Add the stats.js script
            app_index = app_index.replace(
                match[0],
                """<script type="application/javascript">
    // Load stats.js and add it to the page
    (
        function () {
            var script = document.createElement('script');
            script.onload = function() {
                var stats = new Stats();
                stats.dom.style.left = '__LEFT__px';
                stats.dom.style.top = '__TOP__px';
                stats.dom.style.opacity = '__OPACITY__';
                stats.dom.style.zIndex = '__Z_INDEX__';
                document.body.appendChild(stats.dom);
                requestAnimationFrame(
                    function loop() {
                        stats.update();
                        requestAnimationFrame(loop)
                    }
                );
            };
            script.src = '__SCRIPT_SRC__';
            document.head.appendChild(script);
        }
    )();
</script>
""".replace("__SCRIPT_SRC__", script_src)
                .replace("__LEFT__", str(left))
                .replace("__TOP__", str(top))
                .replace("__OPACITY__", str(opacity))
                .replace("__Z_INDEX__", str(zIndex))
                + match[0],
            )

        return app_index
