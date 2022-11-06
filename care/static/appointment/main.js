(function() {
    ('#dp').datepicker();
  });


    // tell the embed parent frame the height of the content
    if (window.parent && window.parent.parent){
      window.parent.parent.postMessage(["resultsFrame", {
        height: document.body.getBoundingClientRect().height,
        slug: "u47d96aq"
      }], "*")
    }

    // always overwrite window.name, in case users try to set it manually
    window.name = "result"
