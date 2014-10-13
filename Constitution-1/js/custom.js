//JavaScript Document
(function($){ 
	//navigation menu 
	var sections=$("#content>section");
	var headerOffset=$("header").outerHeight(true)-5;
	var extraOffset=Math.floor($(window).height()/4);
	var navMenuSel="#navigation-menu";
	var navMenuCurrSelClass="current-section";
	$.fn.NavigationMenu=function(speed,easing){
		var $this=$(this);
		var topPosition=$this.position().top;
		var updatePosition;
		$(window).scroll(function(){
			updatePosition=$(this).scrollTop()+topPosition;
			$this.stop(true,false).animate({top:updatePosition},speed,easing);
			$().NavigationMenuHighlight();
		});
	}
	$.fn.NavigationMenuHighlight=function(){
		var wScroll=$(window).scrollTop();
		sections.each(function(){
			var $this=$(this);
			var $id=$this.attr("id");
			var currMenuOption=$(navMenuSel+" a[href='#"+$id+"']");
			if(wScroll>=$this.offset().top-extraOffset && wScroll<$this.offset().top+($this.height()-extraOffset) && wScroll>headerOffset){
				currMenuOption.stop(true,true).addClass(navMenuCurrSelClass);
			}else{
				currMenuOption.stop(true,true).removeClass(navMenuCurrSelClass);
			}
		});
	}
})(jQuery);