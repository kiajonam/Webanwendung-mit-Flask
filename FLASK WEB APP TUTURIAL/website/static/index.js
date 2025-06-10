function deleteNote(noteId) {
  fetch("/delete_note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
    headers: {
      "Content-Type": "application/json",
    },
  }).then((_res) => {
    window.location.href = "/";
  });
}
