/*
* @Author: dutrasr
* @Date:   2016-08-22 01:06:09
* @Last Modified by:   dutrasr
* @Last Modified time: 2016-08-26 02:14:40
*/

$(document).ready(function(){
	$('.dropdown-button').dropdown();

	$("#er-button").click(function(){
		//$(".hidden-content").hide();
		$(".er-show").toggle();
		$(".wr-show").hide();
		$(".c-show").hide();
		$(".cn-show").hide();
	});
	
	$("#wr-button").click(function(){
		//$(".hidden-content").hide();
		$(".wr-show").toggle();
		$(".er-show").hide();
		$(".c-show").hide();
		$(".cn-show").hide();
	});
	
	$("#c-button").click(function(){
		//$(".hidden-content").hide();
		$(".c-show").toggle();
		$(".wr-show").hide();
		$(".er-show").hide();
		$(".cn-show").hide();
	});

	$("#cn-button").click(function(){
		//$(".hidden-content").hide();
		$(".cn-show").toggle();
		$(".wr-show").hide();
		$(".c-show").hide();
		$(".er-show").hide();
	});
});