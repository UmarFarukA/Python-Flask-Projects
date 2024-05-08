$(document).ready(function () {
  // Handling Adding cabin form
  $("#addForm").submit(function (e) {
    e.preventDefault();
    var formData = $(this).serialize();

    $.ajax({
      type: "POST",
      url: "/add",
      data: formData,
      success: function (res) {
        $("#default-modal").hide();
      },
      error: function (xhr, status, error) {
        alert("Error: " + xhr.responseText);
      },
    });
  });
});
