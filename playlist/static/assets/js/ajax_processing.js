/*global $ */
'use strict';

$(document).ready(function () {
    $('#company-listings').DataTable({
        dom: '<"top"f>rt<"bottom"lpi><"clear">',
        pageLength: 5,
        responsive: true,
        info: false,
        columnDefs: [{
            orderable: false,
            targets: -1
        },],
        lengthMenu: [10, 25, 50, 100],
        pageLength : 10,


        "language":
        {
            "processing": "<b><i class='fa fa-refresh fa-spin loader' ></i>&nbsp;Loading....</b>",
            "searchPlaceholder": "Search",
            "search":"",
            "zeroRecords": "No Record Found",

        },
        // Ajax for pagination
        processing: true,
        serverSide: true,
        ajax: {
            url: window.pagination_url,
            type: 'get',
        },
        columns: [
            { data: 'company_name', name: 'company_name' },
            { data: 'address', name: 'address' },
            { data: 'phone', name: 'phone' },
            { data: 'owner__email', name: 'owner__email' },
            { data: 'owner_name', name: 'owner_name' },
            { data: 'status', name: 'status' },
            { data: 'actions', name: 'actions' }
        ],
    });

    $('#employee_listing').DataTable({
        dom: '<"top"f>rt<"bottom"lpi><"clear">',
        pageLength: 5,
        responsive: true,
        info:false,
        columnDefs: [{
            orderable: false,
            targets: -1
        },],
        lengthMenu: [10, 25, 50, 100],
        pageLength : 10,

        "language":
        {
            "processing": "<b><i class='fa fa-refresh fa-spin'></i>&nbsp;Loading....</b>",
            "searchPlaceholder": "Search",
            "search":"",
            "zeroRecords": "No Record Found",

        },
        // Ajax for pagination
        processing: true,
        serverSide: true,
        ajax: {
            url: window.pagination_url,
            type: 'get',
        },
        columns: [
            { data: 'employee_number', name: 'employee_number' },
            { data: 'employee_name', name: 'employee_name' },
            { data: 'status', name: 'status' },
            { data: 'phone', name: 'phone' },
            { data: 'email', name: 'email' },
            { data: 'title', name: 'title' },
            { data: 'wage', name: 'wage' },
            { data: 'shift__shift_name', name: 'shift__shift_name' },
            { data: 'sick_personal_rate_days', name: 'sick_personal_rate_days' },
            { data: 'health_insurance_premium', name: 'health_insurance_premium' },
            { data: 'actions', name: 'actions' }
        ],
    });

    $('#clients_listing').DataTable({
        dom: '<"top"f>rt<"bottom"lpi><"clear">',
        pageLength: 5,
        responsive: true,
        info: false,
        columnDefs: [{
            orderable: false,
            targets: -1
        },],
        lengthMenu: [10, 25, 50, 100],
        pageLength : 10,

        "language":
        {
            "processing": "<b><i class='fa fa-refresh fa-spin'></i>&nbsp;Loading....</b>",
            "searchPlaceholder": "Search",
            "search":"",
            "zeroRecords": "No Record Found",

        },
        // Ajax for pagination
        processing: true,
        serverSide: true,
        ajax: {
            url: window.pagination_url,
            type: 'get',
        },
        columns: [
            { data: 'client_name', name: 'client_name' },
            { data: 'status', name: 'status' },
            { data: 'address', name: 'address' },
            { data: 'phone', name: 'phone' },
            { data: 'website', name: 'website' },
            { data: 'actions', name: 'actions' }
        ],
    });

    $('#projects_listing').DataTable({
        dom: '<"top"f>rt<"bottom"lpi><"clear">',
        pageLength: 5,
        responsive: true,
        info: false,
        columnDefs: [{
            orderable: false,
            targets: -1
        },],
        lengthMenu: [10, 25, 50, 100],
        pageLength : 10,

        "language":
        {
            "processing": "<b><i class='fa fa-refresh fa-spin'></i>&nbsp;Loading....</b>",
            "searchPlaceholder": "Search",
            "search":"",
            "info":"",
            "zeroRecords": "No Record Found",

        },
        // Ajax for pagination
        processing: true,
        serverSide: true,
        ajax: {
            url: window.pagination_url,
            type: 'get',
        },
        columns: [
            { data: 'project_number', name: 'project_number' },
            { data: 'project_name', name: 'project_name' },
            { data: 'is_sub_job', name: 'is_sub_job' },
            { data: 'client__client_name', name: 'client__client_name' },
            { data: 'project_status__project_status', name: 'project_status__project_status' },
            { data: 'job_estimate', name: 'job_estimate' },
            { data: 'actions', name: 'actions' }
        ],
    });

    $('#work_history_listing').DataTable({
        dom: '<"top"f>rt<"bottom"lpi><"clear">',
        pageLength: 5,
        responsive: true,
        info:false,
        columnDefs: [{
            orderable: false,
            targets: [4,7,8,9]
        },],
        lengthMenu: [10, 25, 50, 100],
        pageLength : 10,

        "language":
        {
            "processing": "<b><i class='fa fa-refresh fa-spin'></i>&nbsp;Loading....</b>",
            "searchPlaceholder": "Search",
            "search":"",
            "zeroRecords": "No Record Found",

        },
        // Ajax for pagination
        processing: true,
        serverSide: true,
        ajax: {
            url: window.pagination_url,
            type: 'get',
        },
        columns: [
            { data: 'employee__employee_name', name: 'employee__employee_name' },
            { data: 'project__project_number', name: 'project__project_number' },
            { data: 'project__client__client_name', name: 'project__client__client_name' },
            { data: 'project__work_description', name: 'project__work_description' },
            { data: 'status', name: 'status' },
            { data: 'start_time', name: 'start_time' },
            { data: 'end_time', name: 'end_time' },
            { data: 'date', name: 'date' },
            { data: 'total_time', name: 'total_time' },
            { data: 'actions', name: 'actions' }
        ],
    });
});
