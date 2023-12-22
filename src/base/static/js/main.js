function make_pdf() {
  const pdfSec = $("#generate-pdf").html();
  let opt = {
    margin: 0.5,
    filename: "download.pdf",
    pagebreask: { avoid: "section" },
    image: { type: ["jpeg", "png"], quality: 0.95 },
    html2canvas: { scale: 2 },
    jsPDF: { unit: "in", format: "a4", orientation: "portrait" },
  };
  let status = html2pdf().from(pdfSec).set(opt).save();
}
