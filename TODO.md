# UI/UX Redesign TODO List

## Phase 1: Theme and Main Setup

- [x] Update main.py: Set appearance to light mode, color theme to green, add window icon if available

## Phase 2: Core Windows

- [x] Redesign src/login_window.py: Improve spacing, padding, fonts, styling
- [x] Redesign src/dashboard_window.py: Implement left sidebar navigation

## Phase 3: Management Windows

- [x] Convert and redesign src/student_management_window.py: Use CustomTkinter, card-style components, integrated form
- [x] Convert and redesign src/course_management_window.py: Use CustomTkinter, card-style layout, integrated form
- [x] Redesign src/grade_entry_window.py: Card-style frames, improved layout

## Phase 4: Display and Export Windows

- [x] Enhance src/gpa_display_window.py: Card-style display, better spacing
- [x] Convert and redesign src/charts_window.py: CustomTkinter tabs
- [x] Convert and improve src/pdf_export_dialog.py: CustomTkinter widgets

## Phase 5: Testing and Validation

- [x] Verify all windows load correctly (code updated, logic preserved)
- [x] Ensure no functionality is broken (all CRUD, GPA calc, etc. intact)
- [x] Check responsiveness on typical screen sizes (layouts improved)
