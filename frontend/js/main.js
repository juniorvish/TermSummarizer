document.addEventListener("DOMContentLoaded", () => {
  const termsUrlInput = document.getElementById("terms_url_input");
  const submitButton = document.getElementById("submit_button");
  const summaryOutput = document.getElementById("summary_output");
  const safetyOutput = document.getElementById("safety_output");

  submitButton.addEventListener("click", submitUrl);

  async function submitUrl() {
    const url = termsUrlInput.value;
    if (!url) {
      alert("Please enter a valid URL");
      return;
    }

    try {
      const response = await fetch("/summarize", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url }),
      });

      if (response.ok) {
        const data = await response.json();
        displaySummary(data.summary);
        displaySafetyRemark(data.safety_remark);
      } else {
        alert("Error: Unable to fetch summary and safety remark");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Error: Unable to fetch summary and safety remark");
    }
  }

  function displaySummary(summary) {
    summaryOutput.textContent = summary;
  }

  function displaySafetyRemark(safetyRemark) {
    safetyOutput.textContent = safetyRemark;
  }
});