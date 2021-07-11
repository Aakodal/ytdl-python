const form = document.getElementById("form");

form.addEventListener("submit", () => {
	document.getElementById("dl-text").hidden = false;
});


const metadataButton = document.getElementById("metadata-label");

metadataButton.addEventListener("click", () => {
	const metadataBlock = document.getElementById("metadata");

	metadataButton.innerText = metadataBlock.hidden ? "▲ Metadata" : "▼ Metadata";
	metadataBlock.hidden = !metadataBlock.hidden;
});
